import numpy as np
import onnxruntime as rt
import onnx
from utils.image_transform import image_transform_onnx


# Load the ONNX model
model = onnx.load('babymodel.onnx')

# Check that the IR is well formed
print(onnx.checker.check_model(model))

np.set_printoptions(suppress=True)

labels = ['baby', 'person']


# get image as tensor - 1 x 3 x 256 x 256 dimensions
baby_tensor_onnx = image_transform_onnx('../images/baby-test.jpg', 255)
adult_tensor_onnx = image_transform_onnx('../images/adult-test2.jpg', 255)

# initialize onnx runtime inference session
sess = rt.InferenceSession('babymodel.onnx')

# input & output names
input_name = sess.get_inputs()[0].name
output_name = sess.get_outputs()[0].name

# input dimensions (important for debugging)
input_dims = sess.get_inputs()[0].shape

results = sess.run([output_name], {input_name: baby_tensor_onnx})[0]
print(labels[np.argmax(results)], results)

results = sess.run([output_name], {input_name: adult_tensor_onnx})[0]
print(labels[np.argmax(results)], results)
# baby [[0.9791235  0.02087651]]
# person [[0.00125656 0.9987435 ]]
# pretty close numbers to pytorch model