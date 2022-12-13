import json
import os
import io
import tarfile
import boto3
import logging
import torch
import torchvision.transforms as transforms
from PIL import Image

# Define logger class
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# load the S3 client when lambda execution context is created
s3 = boto3.client('s3')

# classes for the image classification
classes = []

# Helper function to download object from S3 Bucket
def DownloadFromS3(bucket:str, key:str):
    s3 = boto3.client('s3')
    test_features = s3.download_file(Bucket=bucket, Key=key, Filename=key)
    #img location
    return key 

# get bucket name from ENV variable
# MODEL_BUCKET=os.environ.get('MODEL_BUCKET')
MODEL_BUCKET = "YOUR-BUCKET-HERE"
logger.info(f'Model Bucket is {MODEL_BUCKET}')
MODEL_KEY = "models/model.tar.gz"   
# get bucket prefix from ENV variable
# MODEL_KEY=os.environ.get('MODEL_KEY')

logger.info(f'Model Prefix is {MODEL_KEY}')

# processing pipeline to resize, normalize and create tensor object
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

def load_model():
    """Loads the PyTorch model into memory from a file on S3.

    Returns
    ------
    Vision model: Module
        Returns the vision PyTorch model to use for inference.
    
    """      
    global classes
    logger.info('Loading model from S3')
    obj = s3.get_object(Bucket=MODEL_BUCKET, Key=MODEL_KEY)
    bytestream = io.BytesIO(obj['Body'].read())
    tar = tarfile.open(fileobj=bytestream, mode="r:gz")
    for member in tar.getmembers():
        if member.name.endswith(".txt"):
            print("Classes file is :", member.name)
            f=tar.extractfile(member)
            classes = f.read().splitlines()
            print(classes)
        if member.name.endswith(".pth"):
            print("Model file is :", member.name)
            f=tar.extractfile(member)
            print("Loading PyTorch model")
            model = torch.jit.load(io.BytesIO(f.read()), map_location=torch.device('cpu')).eval()
    return model

# Load model into memory
logger.info('Loading model from file...')
# model = load_model()
model = torch.jit.load("/models/model.tar.gz")
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
