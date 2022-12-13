from fastai.vision.all import *

def model(image_path):
    model = load_learner('babymodel.pkl')# l

    vocab = ['child', 'adult']
    prepped_img = PILImage.create(image_path)
    _,_,probs = model.predict(prepped_img)
    res = list(zip(vocab, [prob.item() for prob in probs]))

    return res