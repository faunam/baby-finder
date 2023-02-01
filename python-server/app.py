from flask import Flask, request
# from model import classify_image
from model import label_photos
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

@app.route('/model', methods=['POST'])
@cross_origin()
def classify_list():
    # mediaItems is  a list of the following format:
            # { media: [
    #       {
    #           baseUrl: ...,
#               filename: "PXL_20230119_232019676.jpg",
#               id: "AOrfjIOcznt5QAmrvgG1b5AB1Qn6bVdVDEe4FSREZBxQRxXpG6DhmOkjunl3a22YHopImgsZqyfF3AyW5GYZMnPGRY35m2tl3A"
#               mediaMetadata: {creationTime: '2023-01-19T23:20:19Z', width: '3024', height: '4032', photo: {…}}
#               mimeType: "image/jpeg",
#               productUrl: ...
#           },
    #  ...]}
    print(request.json)
    body = request.json
    photos = body["mediaItems"]

    labeled_photos = label_photos(photos)

    return labeled_photos


@app.route('/sample', methods=['POST'])
@cross_origin()
def get_sample():
    body = request.json
    with open("ex.json", 'w') as outfile:
        outfile.write(json.dumps(body))
    
    return "all good!"