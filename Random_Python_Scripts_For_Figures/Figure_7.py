import matplotlib.pyplot as plt
import numpy as np

train_averages = [4844.639, 142.396, 5888.199, 312.950]
labels = ["train set non ball", "train set ball", "test set non ball", "test set ball"]

plt.ylabel('Average Bounding Box Size(Area)')
plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='x-large'  
)
plt.text(0,4844.639, 4844.639, ha="center", va="bottom")
plt.text(1,142.396, 142.396, ha="center", va="bottom")
plt.text(2,5888.199, 5888.199, ha="center", va="bottom")
plt.text(3,312.950, 312.950, ha="center", va="bottom")
plt.title("Bounding Boxes Size Distribution(Smaller sub-dataset)")
plt.bar(labels, train_averages)
plt.show()
print("finished")


#####

mydict = {'7': 1, '9': 1}


plt.ylabel('Number of samples')
plt.xlabel('GameID')
plt.title("Game Samples Distribution(Smaller sub-dataset)")
plt.bar(mydict.keys(), mydict.values())
plt.text(0,1, 1, ha="center", va="bottom")
plt.text(1,1, 1, ha="center", va="bottom")
plt.show()