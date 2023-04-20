import matplotlib.pyplot as plt
import numpy as np

train_averages = [5188.928, 199.381, 6440.6443, 297.166]
labels = ["train set non ball", "train set ball", "test set non ball", "test set ball"]

plt.ylabel('Average Bounding Box Size')
plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='x-large'  
)
plt.text(0,5188.928, 5188.928, ha="center", va="bottom")
plt.text(1,199.381, 199.381, ha="center", va="bottom")
plt.text(2,6440.6443, 6440.6443, ha="center", va="bottom")
plt.text(3,297.166, 297.166, ha="center", va="bottom")
plt.title("Bounding Boxes Size Distribution")
plt.bar(labels, train_averages)
plt.show()
print("finished")