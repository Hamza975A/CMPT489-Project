import os
import configparser
import matplotlib.pyplot as plt

config_reader = configparser.ConfigParser()

filename="gameinfo.ini"

rootdir = '/mnt/g/SoccerNet_Data/Dataset/tracking-2023/train/train'

actionClassCount = {}

for subdir, dirs, files in os.walk(rootdir):
    if(dirs and subdir is not rootdir): #Only use immediate folders
        path = os.path.join(subdir, filename)
        config_reader.read(path)
        actionClass = config_reader['Sequence']['actionClass']
        if actionClass in actionClassCount:
            actionClassCount[actionClass] +=1
        else:
            actionClassCount[actionClass] = 1

print(actionClassCount)

rootdir2 = '/mnt/g/SoccerNet_Data/Dataset/tracking-2023/test/test'
actionClassCount = {}

for subdir, dirs, files in os.walk(rootdir2):
    if(dirs and subdir is not rootdir2): #Only use immediate folders
        path = os.path.join(subdir, filename)
        config_reader.read(path)
        actionClass = config_reader['Sequence']['actionClass']
        if actionClass in actionClassCount:
            actionClassCount[actionClass] +=1
        else:
            actionClassCount[actionClass] = 1

print(actionClassCount)

plt.bar(actionClassCount.keys(), actionClassCount.values())
plt.show(block=True)
print("Done")
