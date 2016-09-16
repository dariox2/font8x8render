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
img = plt.imread('demo_0_original.jpg')


# demo 1: simple, horizontal, red
#text="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
#font8x8render.annotate_img(img, text, x=30, y=60, color=[255,0,0])

# demo 2: from right margin, vertical, zoom 2x, transparency
#text="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
#font8x8render.annotate_img(img, text, x=-30, y=15, color=[0,255,0],
#                              zoom=2, dir="vert", alpha=0.5)

# demo 3: timestamp with background box
text=datetime.date.today().strftime("%Y-%m-%d")+" "+ \
     datetime.datetime.now().time().strftime("%H:%M:%S")
font8x8render.annotate_img(img, text, x=50, y=50,
      color=[255,255,255], alpha=0.6, zoom=1, box="black")



plt.imshow(img)
plt.show()

plt.imsave(fname='demo_annotated.png', arr=img)

warnings.simplefilter('ignore')
plt.pause(10)

plt.close()

quit()

# eop


