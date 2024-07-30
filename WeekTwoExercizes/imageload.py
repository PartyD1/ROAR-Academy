import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np


lenna_img = mpimg.imread('lenna.png')


flag_img = Image.open('flag.png')


lenna_height, lenna_width, _ = lenna_img.shape
flag_img = flag_img.resize((lenna_width, lenna_height))


flag_array = np.array(flag_img)


lenna_img[:flag_array.shape[0], -flag_array.shape[1]:] = flag_array


plt.imshow(lenna_img)
plt.axis('off')  
plt.show()
