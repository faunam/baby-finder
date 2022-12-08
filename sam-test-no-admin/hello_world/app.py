import json
import boto3
import logging
import torch
import torchvision.transforms as transforms
from PIL import Image

# Define logger class
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Helper function to download object from S3 Bucket
def DownloadFromS3(bucket:str, key:str):
    s3 = boto3.client('s3')
    test_features = s3.download_file(Bucket=bucket, Key=key, Filename=key)
    #img location
    return key 

# Load model into memory
logger.info('Loading model from file...')

model = torch.load('/models/baby-torch.pkl')# load model
model.eval()
logger.info('Model Loaded from file...')

def image_transform(path: str, size: int) -> torch.Tensor:
    '''Helper function to transform image.'''
    image = Image.open(path)
    # transformation pipeline
    transformation = transforms.Compose([
                transforms.Resize([size,size]), # resizes image
                transforms.ToTensor() # converts to image to tensor
            ])
    image_tensor = transformation(image).unsqueeze(0)

    return image_tensor

def lambda_handler(event, context):

    # Read JSON data packet
    data = json.loads(event['body'])
    bucket = data['bucket']
    key = data['key']

    # Load test data from S3
    logger.info(f'Loading data from {bucket}/{key}')
    filepath = DownloadFromS3(bucket, key)
    logger.info(f'Loaded {type(key)} from S3...')

    #  Perform predictions and return predictions as JSON.
    logger.info(f'Classifying...')

    vocab = ['child', 'adult']
    tensor = image_transform(filepath, 255)
    with torch.no_grad():
        results = model(tensor)
    results_list = results.detach().tolist()[0]
    res = list(zip(vocab, results_list))

    body = {"data": res}
    response_body = json.dumps(body)

    return {
        'statusCode': 200,
        'headers':{
            'Content-type':'application/json'
        },
        'body': response_body
    }
