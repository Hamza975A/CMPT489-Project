import matplotlib.pyplot as plt
import numpy as np

image_sizes = {
    "{1080, 1920, 3}": 107250
}


plt.ylabel("Number of images")
plt.xticks(
    fontweight='light',
    fontsize='x-large'  
)
plt.text(0,107250, 107250, ha="center", va="bottom")

plt.title("Image Size Distribution")
plt.bar(image_sizes.keys(), image_sizes.values())
plt.show()
print("finished")