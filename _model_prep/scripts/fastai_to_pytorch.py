import torch
import torchvision.transforms as transforms
from fastai.vision.all import *

# load FastAI ResNet model
learn = load_learner('models/babymodel.pkl')

# print('adult test', learn.predict('../images/adult-test.jpg'))
# print('baby test', learn.predict('../images/baby-test.jpg'))
# so far so good, looks the same as colab

# check the transformations applied to the model; looks the same as their example.
# print(learn.dls.transform)
# >> [[noop:
# encodes: (object,object) -> noopdecodes: , PILBase.create:
# encodes: (Path,object) -> create
# (str,object) -> create
# (Tensor,object) -> create
# (ndarray,object) -> create
# (bytes,object) -> createdecodes: ], parent_label:
# encodes: (object,object) -> parent_labeldecodes: ]

# get PyTorch model
# .model attribute stores the model
# .eval() sets the model into evaluation mode - no backward propagation
pytorch_model = learn.model.eval()

# define softmax layer
softmax_layer = torch.nn.Softmax(dim=1) # define softmax

# define normalization layer
normalization_layer = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

# assemble the final model
final_model = nn.Sequential(
    normalization_layer,
    pytorch_model,
    softmax_layer
)
