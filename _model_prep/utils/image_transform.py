from PIL import Image
import torchvision.transforms as transforms
import torch
import numpy as np


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

def image_transform_onnx(path: str, size: int) -> np.ndarray:
    '''Image transform helper for onnx runtime inference.'''

    image = Image.open(path)
    image = image.resize((size,size))

    # now our image is represented by 3 layers - Red, Green, Blue
    # each layer has a 224 x 224 values representing
    image = np.array(image)

    # dummy input for the model at export - torch.randn(1, 3, 224, 224)
    image = image.transpose(2,0,1).astype(np.float32)

    # our image is currently represented by values ranging between 0-255
    # we need to convert these values to 0.0-1.0 - those are the values that are expected by our model
    image /= 255
    image = image[None, ...]
    return image
