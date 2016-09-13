#
# example (3): annotate image with 8x8 font lib
#

#import numpy as np
import matplotlib.pyplot as plt

import font8x8

img = plt.imread('babyfox1.jpg')

font8x8.annotate_img(img)

plt.imshow(img)
plt.show()

plt.imsave(fname='annotate2_test.png', arr=img)


