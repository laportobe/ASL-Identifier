Sign Language Predictor Model

This model is used to predict American Sign Language (ASL) signs based on input from a USB camera. It is trained on an imagenet Resnet-18 model using transfer learning. The goal of this project is improving communication between mute and deaf individuals and the general population.

![A computer analyzes a face.](https://imgur.com/HeyVfsW)

## The Algorithm
The algorithim is used by recording a video on a Logitech webcam - supported by Jetson nano. It uses a 2GB Jetson Nano, and so it uses a preflashed SD card flashed from the NVIDIA webpage. It collects frames from the live video and sends the frames to be compared to pre-identified letters in the ASL alphabet using imagenet. From these comparisons, imagenet will then make a prediction for which letter is being signed. The model will then print that prediction along with a confidence percentage and based on that confidence level it is up to user interpretation to decide the validity of the prediction.
Note: I ran this model on a relatively low epoch with information that was askew. The pretrained model is quite inaccurate.
## Running this project

1. Connect to your Jetson Nano via VSCODE. 
2. Connect your Webcam (preferably logitech)
3. Be sure to download all files from the ver_1 folder, including all resnet18 files and labels.txt, as well as the video.py, which will be found outside of that folder.
4. On the preflashed SD card, there should be a docker container, which is required for the implementation of this model. To enter the docker container, change directories into jetson-inference/build/aarch64/bin. - use this code if you're in the home.$: cd jetson-inference/build/aarch64/bin, and run this code -$ ./docker/run.sh --volume /home/(username)/final-projects:/final-projects

- the code moves the final-projects folder into the docker container so that the line from PIL import Image runs without an error.

6a. Finally run the following code - $ python3 video.py (webcam name here). You should start to immediately see output from this command.
7. The model is up and running, start signing for predictions!

[View a video explanation here](https://youtu.be/g91S_Gbns6w)
