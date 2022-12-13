import json
import requests
# import numpy as np

bucket_name = 'YOUR-BUCKET-HERE'
key =  'adult-test2.jpg'

data = {
    'bucket':bucket_name,
    'key':key,
}

headers = {
    'Content-type': "application/json"
}

# Main code for post HTTP request
url = "http://127.0.0.1:3000/hello"
response = requests.request("POST", url, headers=headers, data=json.dumps(data))

print(response.json())

# Show confusion matrix and display accuracy
# lambda_predictions = np.array(response.json())
# show_cm(test_target, lambda_predictions, range(10))