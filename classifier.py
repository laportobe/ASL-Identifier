import sys
import argparse

from jetson_inference import actionNet
from jetson_utils import videoSource, videoOutput, cudaFont, Log

import process_input as img

while True:
    class_id, confidence = NET.Classify(img)
    class_desc = NET.GetClassDesc(class_id)
    print(class_desc)