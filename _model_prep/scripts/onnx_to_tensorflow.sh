#!/bin/bash
# required modules: onnx_tf, tensorflow, tensorflow_probability
onnx-tf convert -i models/babymodel.onnx -o models/babymodel_tf

