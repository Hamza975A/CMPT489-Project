import os
import configparser
import matplotlib.pyplot as plt
from statistics import mean 

config_reader = configparser.ConfigParser()

filename="gt/gt.txt"

rootdir = '/mnt/g/SoccerNet_Data/Dataset/tracking-2023/train/train'

tracklets_sizes = []


for subdir, dirs, files in os.walk(rootdir):
    if(dirs and subdir is not rootdir): #Only use immediate folders
        path = os.path.join(subdir, filename)
        file1 = open(path, 'r')
        Lines = file1.readlines()
        current_ID = "1"
        counter = 0
        total_size = 0
        for line in Lines:
            line = line.split(',')
            if current_ID != line[1]:
                tracklets_sizes.append(total_size/counter)
                current_ID = line[1]
                counter = 0
                total_size = 0

            counter+=1
            total_size+=(int(line[4]) * int(line[5]))



#print(tracklets_sizes)
tracklets_sizes.sort(reverse=True)
balls = tracklets_sizes[-57:]
tracklets_sizes = tracklets_sizes[:-57]
#print(tracklets_sizes)

tracklets_train = mean(tracklets_sizes)
ball_train = mean(balls)
print(tracklets_train)
print(ball_train)


rootdir2 = '/mnt/g/SoccerNet_Data/Dataset/tracking-2023/test/test'
tracklets_sizes = []

for subdir, dirs, files in os.walk(rootdir2):
    if(dirs and subdir is not rootdir2): #Only use immediate folders
        path = os.path.join(subdir, filename)
        file1 = open(path, 'r')
        Lines = file1.readlines()
        current_ID = "1"
        counter = 0
        total_size = 0
        for line in Lines:
            line = line.split(',')
            if current_ID != line[1]:
                tracklets_sizes.append(total_size/counter)
                current_ID = line[1]
                counter = 0
                total_size = 0

            counter+=1
            total_size+=(int(line[4]) * int(line[5]))

tracklets_sizes.sort(reverse=True)
balls = tracklets_sizes[-57:]
tracklets_sizes = tracklets_sizes[:-57]
#print(tracklets_sizes)

tracklets_train = mean(tracklets_sizes)
ball_train = mean(balls)
print(tracklets_train)
print(ball_train)

print("Done")
