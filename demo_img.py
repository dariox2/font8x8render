#
# example: annotate image with date & time using 8x8 font
#
# Author: Dario Albertocchi, 2016-09-12 (Programmer's Day)
# License: Public Domain
#
#

import matplotlib.pyplot as plt
import warnings
import datetime

import font8x8render

plt.ion()
img = plt.imread('anu.jpg')

#text="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
text=datetime.date.today().strftime("%Y-%m-%d")+" "+datetime.datetime.now().time().strftime("%H:%M:%S")
font8x8render.annotate_img(img, text, x=50, y="bottom",
      color=[255,255,255], alpha=0.6, zoom=1)

plt.imshow(img)
plt.show()

plt.imsave(fname='demo_img_annotated.png', arr=img)

warnings.simplefilter('ignore')
plt.pause(10)

plt.close()

quit()

# eop


