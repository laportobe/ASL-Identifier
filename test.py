#!/usr/bin/python3
import jetson_inference
from jetson_inference import imageNet
import jetson_utils

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="filename of the image to process")
parser.add_argument("--network", type=str, default="resnet-18", help="model to use, can be:  googlenet, resnet-18, ect. (see --help for others)")
# parser.add_argument("--model", type=str)
opt = parser.parse_args()

while True:
    img = jetson_utils.loadImage(opt.filename)

    net = imageNet(model="resnet18.onnx", labels="labels.txt", 
                    input_blob="input_0", output_blob="output_0")

    # net = jetson_inference.imageNet(opt.network, opt.model)
    #
    class_idx, confidence = net.Classify(img)

    class_desc = net.GetClassDesc(class_idx)
    print("image is recognized as '{:s}' (class #{:d}) with {:f}% confidence".format
        (class_desc, class_idx, confidence * 100))
