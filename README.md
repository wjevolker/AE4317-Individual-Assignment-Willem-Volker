# AE4317-Individual-Assignment-Willem-Volker
# In this readme file the reader can find how to reproduce the outputs I created for my AE4317 Autonomous Flight of Micro Air Vehicles individual assignment.

# First, training the neural network: YOLOv3-tiny. For this the Darknet repository has been used. 

# Installation of Darknet can be done with the following commands:

git clone https://github.com/pjreddie/darknet.git
cd darknet
make

# If you run the following command

./darknet

# You should see the following:

usage: ./darknet <function>
  
# For some functions we will need OpenCV, so in the makefile change 

OPENCV=1

# The next step is to create the image annotation files in YOLO format

