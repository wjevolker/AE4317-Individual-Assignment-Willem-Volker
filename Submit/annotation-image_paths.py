#Script to generate the files train.txt and test.txt
#containing the path to the images used for training and testing
#Add your own image paths in lines 28 and 35

import csv
import os

testlist = []
for i in range(0,699,5):
    testlist.append(i)

memory = []
with open('corners.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    linecount = 0
    traincount = 0
    testcount = 0
    for row in csv_reader:
        name = row[0]
        linecount += 1
              
        if name in memory:
            x = 'skip'
        else:
            newname = name[:-4]+'.jpg\n'
            if linecount not in testlist:
                f = open('train.txt','a')
                line = r'add-your-own-image-path' + newname 
                f.write(line)
                f.close()
                memory.append(name)
                traincount += 1
            else:
                f = open('test.txt','a')
                line = r'add-your-own-image-path' + newname
                f.write(line)
                f.close()
                memory.append(name)
                testcount += 1
