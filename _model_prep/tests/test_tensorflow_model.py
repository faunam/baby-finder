import tensorflow as tf

loaded = tf.saved_model.load("models/babymodel_tf")
print(list(loaded.signatures.keys()))

infer = loaded.signatures["serving_default"]
print(infer.structured_outputs)

img = tf.keras.utils.load_img('images/baby-test.jpg', target_size=[255, 255])

baby_test = tf.keras.utils.img_to_array(img)

# baby_test = tf.keras.applications.mobilenet.preprocess_input(
#     baby_test[tf.newaxis,...])

test_tensor = tf.constant(baby_test)
print(test_tensor.shape)

labeling = infer(test_tensor) # [pretrained_model.output_names[0]]
print(labeling)

# decoded = imagenet_labels[np.argsort(labeling)[0,::-1][:5]+1]

# print("Result after saving and loading:\n", decoded)


