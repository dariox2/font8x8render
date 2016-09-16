#
# example: annotate image with text using 8x8 font
#
# Author: Dario Albertocchi
# License: Public Domain
#
#

import matplotlib.pyplot as plt
import warnings
import datetime

import font8x8render

plt.ion()
img = plt.imread('demo_orig.jpg')

text="ABCabc123aaaaaaaaaaaaaaaabbbbbbbbbbbbbbccc"
font8x8render.annotate_img(img, text, x=30, y=-30, color=[0,0,0], alpha=0.5,
                             box="white", dir="vert")

plt.imshow(img)
plt.show()

plt.imsave(fname='demo_annotated.png', arr=img)

warnings.simplefilter('ignore')
plt.pause(10)

plt.close()

quit()

# eop


