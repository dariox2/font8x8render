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

text="BARK BARK BARK! BARK bark! bark bark bark bark!"
font8x8render.annotate_img(img, text, x=90, y=-100, color=[0,0,0], alpha=0.5,
                             box="white", zoom=1)#, dir="vert")

plt.imshow(img)
plt.show()

plt.imsave(fname='demo_annotated.png', arr=img)

warnings.simplefilter('ignore')
plt.pause(10)

plt.close()

quit()

# eop


