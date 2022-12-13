
def classify_photo(photo):
    pass

import json
import boto3
import logging

# Define logger class
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Helper function to download object from S3 Bucket
def DownloadFromS3(bucket:str, key:str):
    s3 = boto3.client('s3')
    test_features = s3.download_file(Bucket=bucket, Key=key, Filename=key)
    #img location
    return key

# UNCOMMENT PLEASE
# Load model into memory
# logger.info('Loading model from file...')
# model = load_learner('babymodel.pkl')# load model
# logger.info('Model Loaded from file...')

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
    # for loop running through multiple images or what?
    vocab = ['child', 'adult']
    # prepped_img = PILImage.create(filepath)
    # UNCOMMENT PlZ
    # _,_,probs = model.predict(prepped_img)
    # res = list(zip(vocab, [prob.item() for prob in probs]))
    res = [bucket, key]
    body = {"data": res}

    # mock = {"data": ["baby", "baby", "adult"]}
    response_body = json.dumps(body)

    return {
        'statusCode': 200,
        'headers':{
            'Content-type':'application/json'
        },
        'body': response_body
    }
