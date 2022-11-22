import torch
from fastai.vision.all import np

from utils.image_transform import image_transform
from scripts.fastai_to_pytorch import final_model


labels = ['baby', 'person']

# run pytorch inference on test images
# i thought the image size for my model was 128 but putting 255 made the results a lot better here.
baby_tensor_pytorch = image_transform('../images/baby-test.jpg', 255)
adult_tensor_pytorch = image_transform('../images/adult-test2.jpg', 255)

with torch.no_grad():
    results = final_model(baby_tensor_pytorch)
print(labels[np.argmax(results.detach().numpy())], results.detach().numpy())

with torch.no_grad():
    results = final_model(adult_tensor_pytorch)
print(labels[np.argmax(results.detach().numpy())], results.detach().numpy())
# baby-test:  baby [[0.9823276 0.0176724]]
# adult-test2: person [[0.00126307 0.9987369 ]]