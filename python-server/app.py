from flask import Flask
from model import model

app = Flask(__name__)

@app.route("/model")
def hello_world():
    filepath = "adult-test2.jpg"
    return model(filepath)