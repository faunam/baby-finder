# from this poggers blog post https://dev.to/tkeyo/export-fastai-resnet-models-to-onnx-2gj7
# and check out the corresponding repo for more details https://github.com/tkeyo/fastai-onnx/blob/main/fastai_to_onnx.ipynb
import torch
from scripts.fastai_to_pytorch import final_model # TODO is this going to put me in an infinite import loop?

torch.onnx.export(
    final_model, 
    torch.randn(1, 3, 255, 255),
    'models/babymodel.onnx',
    do_constant_folding=True,
    export_params=True,
    input_names=['image_1_3_255_255'],
    output_names=['baby'],
    opset_version=11
)

# and using this package https://github.com/onnx/onnx-tensorflow
# to convert from onnx to tf