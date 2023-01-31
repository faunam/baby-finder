from flask import Flask, request
# from model import classify_image
import json
from flask_cors import CORS, cross_origin
# cors stuff from this stackoverflow answer https://stackoverflow.com/questions/25594893/how-to-enable-cors-in-flask

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/hello', methods=['GET'])
@cross_origin()
def hello():
    return 'hello world!'

# @app.route('/model', methods=['POST'])
# @cross_origin()
# def classify():
#     print(request.json)
#     body = request.json
#     urls = body["urls"]
#     print(urls)

#     classifications = [classify_image(url) for url in urls]

#     print(classifications)
#     res = list(zip(urls, classifications))
#     print(res)

#     return res

@app.route('/sample', methods=['POST'])
@cross_origin()
def get_sample():
    body = request.json
    with open("ex.json", 'w') as outfile:
        outfile.write(json.dumps(body))
    
    return "all good!"