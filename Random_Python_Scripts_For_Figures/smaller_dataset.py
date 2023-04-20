import os
import configparser
import matplotlib.pyplot as plt
from statistics import mean 

config_reader = configparser.ConfigParser()

file1path = '/mnt/g/SoccerNet_Data/Dataset/tracking-2023/train/train/SNMOT-167/gt/gt.txt'
tracklets_sizes = []

file1 = open(file1path, 'r')
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
balls = tracklets_sizes[-1:]
tracklets_sizes = tracklets_sizes[:-1]
tracklets_train = mean(tracklets_sizes)
ball_train = mean(balls)
print(tracklets_train)
print(ball_train)

file2path = '/mnt/g/SoccerNet_Data/Dataset/tracking-2023/test/test/SNMOT-125/gt/gt.txt'
tracklets_sizes = []

file2 = open(file2path, 'r')
Lines = file2.readlines()
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
balls = tracklets_sizes[-1:]
tracklets_sizes = tracklets_sizes[:-1]
tracklets_train = mean(tracklets_sizes)
ball_train = mean(balls)
print(tracklets_train)
print(ball_train)