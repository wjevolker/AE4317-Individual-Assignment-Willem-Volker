#Script to create the YOLO image annotation files
#A .txt file is created for each image, containing the coordinates of the gate labels

import csv
import os
import cv2
import numpy as np


with open('corners.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        name = row[0]

        img = cv2.imread(name)
        
        x_min = min(int(row[1]),int(row[7])) / len(img[0]) #leftmost point of gate (normalized)
        x_max = max(int(row[3]),int(row[5])) / len(img[0]) #rightmost point of gate (normalized)
        y_min = min(int(row[2]),int(row[4])) / len(img) #topmost point of gate (normalized)
        y_max = max(int(row[6]),int(row[8])) / len(img) #bottommost point of gate (normalized)
        
        x = x_min + (x_max - x_min)/2 #normalized x-coordinate of the center of the object
        y = y_min + (y_max - y_min)/2 #normalized y-coordinate of the center of the object
        width = x_max - x_min #normalized width of the bounding box
        height = y_max - y_min #normalized height of the bounding box
        textname = name[:-4] + '.txt'
        f = open(textname,'a')
        line = '0'+' '+str(x)+' '+str(y)+' '+str(width)+' '+str(height)+'\n'
        f.write(line)
        f.close()

        
            
        

        
