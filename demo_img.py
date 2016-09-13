#
# example: annotate image with 8x8 font
#

import matplotlib.pyplot as plt
import warnings

import font8x8render

plt.ion()
img = plt.imread('anu.jpg')

text="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
font8x8render.annotate_img(img, text, x=50, y=10,
     color=[255,255,0], alpha=0.7)

plt.imshow(img)
plt.show()

plt.imsave(fname='demo_img_annotated.png', arr=img)

warnings.simplefilter('ignore')
plt.pause(3)

plt.close()

quit()

# eop


