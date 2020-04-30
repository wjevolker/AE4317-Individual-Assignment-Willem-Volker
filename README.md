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

# Then change the file yolov3-tiny.cfg in darknet/cfg and replace it with the file in this repo with the same name
# In this file I changed the settings specific for my gate detector

# Now start the training with
./darknet detector train cfg/voc.data cfg/yolov3-tiny.cfg darknet53.conv.74

# The weights will be saved in the darknet/backup folder

# For testing I used the darknet fork by AlexeyAB
# Download it from github.com/AlexeyAB/darknet

# Now place the following files in AlexeyAB's darknet folder
train.txt 
test.txt 
yolov3-tiny.cfg
yolov3_custom_train_10000.weights

# Move to this directory and run the following to calculate mAP at 50% IoU and detection time
./darknet detector map cfg/obj.data yolov3-tiny.cfg yolov3-tiny_10000.weights

# And for mAP at 75%:
./darknet detector map cfg/obj.data yolov3-tiny.cfg yolov3-tiny_10000.weights -iou_thresh 0.75

# To draw the bounding box for a certain image run 
./darknet detector test cfg/obj.data yolov3-tiny.cfg yolov3-tiny_10000.weights -iou_thresh 0.75










