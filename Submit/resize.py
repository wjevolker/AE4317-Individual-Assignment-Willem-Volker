#This file is used to resize the images such that the effect on detector speed
#can be evaluated

import cv2
import csv

with open('corners.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        name = row[0]
        img = cv2.imread(name[:-4] + '.jpg')
        resized = cv2.resize(img, (180,180))
        cv2.imwrite(name[:-4] + '.jpg',resized)
