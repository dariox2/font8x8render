#
# example (3): annotate image with 8x8 font lib
#

#import numpy as np
import matplotlib.pyplot as plt

import font8x8

img = plt.imread('anu.jpg')

text="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
font8x8.annotate_img(img, text, xpos=10, ypos=50, color=[0,255,0], alpha=0.5)

plt.imshow(img)
plt.show()

plt.imsave(fname='demo_img_annotated.png', arr=img)

