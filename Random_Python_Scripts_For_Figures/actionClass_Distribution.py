import matplotlib.pyplot as plt
import numpy as np

data = {'Kick-off': 9, 'Shots on target': 11, 'Foul': 10, 'Offside': 7, 'Shots off target': 12, 'Clearance': 12, 'Direct free-kick': 11, 'Corner': 12, 'Yellow card': 9, 'Substitution': 6, 'Goal': 6, 'Penalty': 1}
classes = ['Kick-off', 'Shots on target', 'Foul', 'Offside', 'Shots off target', 'Clearance', 'Direct free-kick', 'Corner', 'Yellow card', 'Substitution', 'Goal', 'Penalty']
trainActions = [6, 6, 5, 3, 6, 6, 6, 6, 5, 3, 5, 0]
testActions = [3, 5, 5, 4, 6, 6, 5, 6, 4, 3, 1, 1]


plt.xlabel('Number of instances')
#plt.xlabel('x numbers')
plt.yticks(
    np.arange(len(classes)),
    classes,
    fontweight='light',
    fontsize='x-large'  
)
plt.title("actionClass Distribution")
plt.barh(np.arange(len(classes))-0.2, trainActions, height=0.4, label="train")
plt.barh(np.arange(len(classes))+0.2, testActions, height=0.4, label="test")
plt.legend()
plt.show()
print("finished")