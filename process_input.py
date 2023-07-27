#!/usr/bin/python3

import sys
import argparse

from jetson_inference import poseNet
from jetson_utils import videoSource, videoOutput, Log

parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--overlay", type=str, default="links,keypoints", help="pose overlay flags (e.g. --overlay=links,keypoints)\nvalid combinations are:  'links', 'keypoints', 'boxes', 'none'")
parser.add_argument("--network", type=str, default="Pose-ResNet18-Hand")

args = parser.parse_args()
threshold = 0.15

net = imageNet(model="resnet18")

input = videoSource(args.input, argv=sys.argv)
output = videoOutput(args.output, argv=sys.argv)

while True:
    img = input.Capture()
    
     = net.Process(img, overlay=args.overlay)
    output.Render(img)
    
    class_desc = net.GetClassDesc(class_id)
    print(class_desc)

    output.SetStatus("{:s} | Network {:.0f} FPS".format(args.network, net.GetNetworkFPS()))

    net.PrintProfilerTimes()

    if img is None or not input.IsStreaming() or not output.IsStreaming():
        break

def get_overlay():
    return overlay