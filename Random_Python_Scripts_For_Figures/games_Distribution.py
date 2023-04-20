import os
import configparser
import matplotlib.pyplot as plt

config_reader = configparser.ConfigParser()

filename="gameinfo.ini"

rootdir = '/mnt/g/SoccerNet_Data/Dataset/tracking-2023/train/train'

gameIDCount = {}

for subdir, dirs, files in os.walk(rootdir):
    if(dirs and subdir is not rootdir): #Only use immediate folders
        path = os.path.join(subdir, filename)
        config_reader.read(path)
        gameID = config_reader['Sequence']['gameID']
        if gameID in gameIDCount:
            gameIDCount[gameID] +=1
        else:
            gameIDCount[gameID] = 1

print(gameIDCount)

rootdir2 = '/mnt/g/SoccerNet_Data/Dataset/tracking-2023/test/test'
gameIDCount = {}

for subdir, dirs, files in os.walk(rootdir2):
    if(dirs and subdir is not rootdir2): #Only use immediate folders
        path = os.path.join(subdir, filename)
        config_reader.read(path)
        gameID = config_reader['Sequence']['gameID']
        if gameID in gameIDCount:
            gameIDCount[gameID] +=1
        else:
            gameIDCount[gameID] = 1

print(gameIDCount)

print("Done")
