import os
import configparser
import matplotlib.pyplot as plt
import cv2

rootdir = '/mnt/g/SoccerNet_Data/Dataset/tracking-2023/train/train'

image_size_count = {}

for subdir, dirs, files in os.walk(rootdir):
    print("JUMP")
    for file in files:
        if(file.lower().endswith(('.jpg'))):
            im = cv2.imread(os.path.join(subdir, file))
            print(im.shape)
            #if im.shape in image_size_count:
            #    image_size_count[im.shape] +=1
            #else:
            #    image_size_count[im.shape] = 1


print("Half way!")
rootdir2 = '/mnt/g/SoccerNet_Data/Dataset/tracking-2023/test/test'


for subdir, dirs, files in os.walk(rootdir2):
    for file in files:
        
        if(file.lower().endswith(('.jpg'))):
            im = cv2.imread(os.path.join(subdir, file))
            print(im.shape)
            #if im.shape in image_size_count:
            #    image_size_count[im.shape] +=1
            #else:
            #    image_size_count[im.shape] = 1

print("Done")