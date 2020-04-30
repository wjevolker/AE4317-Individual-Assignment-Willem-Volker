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
# 1. We need a text file for each image, containing the gate coordinates in YOLO format
# For this just run my Python script annotation.py

# 2. We also need two files with the train and test image paths
# These can be produced with annotation-image_paths.py

# 3. Create a file obj.names in the directory darknet/data containing just the word 'Gate'

# 4. Create a file obj.data in the directory darknet/data containing 
classes = 1
train  = data/train.txt
valid  = data/test.txt
names = data/obj.names
backup = backup/

# Now download the pre-trained weights with
wget https://pjreddie.com/media/files/darknet53.conv.74

# Then open the file yolov3-tiny.cfg in darknet/cfg and change the following lines
# The number of filters equals (classes + 5)3
# In lines 127, 135, 171 and 177 set 
filters=18






