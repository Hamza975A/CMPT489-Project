import matplotlib.pyplot as plt
import numpy as np

train = {'4': 18, '6': 19, '9': 20}
test = {'7': 16, '8': 19, '11': 14}


plt.ylabel('Number of samples')
plt.xlabel('GameID')
plt.title("Game Samples Distribution(train set)")
plt.bar(train.keys(), train.values(), label="train")
plt.legend()
plt.text(0,18, 18, ha="center", va="bottom")
plt.text(1,19, 19, ha="center", va="bottom")
plt.text(2,20, 20, ha="center", va="bottom")
plt.show()

plt.bar(test.keys(), test.values(), label="test")
plt.legend()
plt.ylabel('Number of samples')
plt.xlabel('GameID')
plt.title("Game Samples Distribution(test set)")
plt.text(0,16, 16, ha="center", va="bottom")
plt.text(1,19, 19, ha="center", va="bottom")
plt.text(2,14, 14, ha="center", va="bottom")
plt.show()
print("finished")