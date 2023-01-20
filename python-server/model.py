from fastai.vision.all import *
from urllib.request import urlretrieve
import os


def model(image_path):
    model = load_learner('babymodel.pkl')# l

    vocab = ['child', 'adult']
    prepped_img = PILImage.create(image_path)
    _,_,probs = model.predict(prepped_img)
    res = list(zip(vocab, [prob.item() for prob in probs]))

    return res

def download_image_from_url(url):
    # goddamnit now i need to parse the url to get the image name
    print("url to download")
    print(url)
    destination = os.path.basename(url)
    urlretrieve(url, destination)
    print(destination)
    return destination

def classify_image(url):
    image_path = download_image_from_url(url)
    return model(image_path)

# from urllib.parse import urlparse

# url = "http://photographs.500px.com/kyle/09-09-201315-47-571378756077.jpg"
# a = urlparse(url)
# print(a.path)                    # Output: /kyle/09-09-201315-47-571378756077.jpg
# print(os.path.basename(a.path)