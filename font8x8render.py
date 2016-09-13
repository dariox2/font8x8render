#
# Render text with 8x8 font over an image
#
# Author: Dario Albertocchi, 2016-09-12 (Programmer's Day)
# License: Public Domain
#

import font8x8

def select_set(ord):
  if ord>=0 and ord<=127:
    bitmap=font8x8.basic[ord]
  elif ord>=160 and ord<=255:
    bitmap=font8x8.ext_latin[ord-160]
  elif ord>=912 and ord<=969:
    bitmap=font8x8greek[ord-912]
  elif ord>=9472 and ord<=9599:
    bitmap=font8x8_box[ord-9472]
  elif ord>=9600 and ord<=9631:
    bitmap=font8x8_block[ord-9600]
  elif ord>=12352 and ord<=12447:
    bitmap=font8x8_hiragana[ord-12352]
  else:
    bitmap=font8x8_basic[32]
    
  return bitmap


def newcol(oldpix, newpix, alpha):

  return [oldpix[0]*(1-alpha)+newpix[0]*alpha,
          oldpix[1]*(1-alpha)+newpix[1]*alpha,
          oldpix[2]*(1-alpha)+newpix[2]*alpha]


def annotate_img(img, text, x=8, y=8, dir="horiz", color=[128,128,128], alpha=1.0):

  kern=8

  dx=0
  dy=0
  for i in range(0, len(text)):

    c=text[i:i+1]
    bitmap = select_set(ord(c))

    # Draw a character
    for posy in range(0,8):
      for posx in range(0,8):
        pixel = bitmap[posy] & 1 << posx
        if pixel != 0:
          # notice inverted coordinates used in arrays
          img[y+dy+posy,x+dx+posx]=newcol(img[y+dy+posy,x+dx+posx], color, alpha)

    if dir=="vert":
      dy+=kern
      if dy>=img.shape[0]-y-8:
        dx+=kern+2
        dy=0
    else:
      dx+=kern
      if dx>=img.shape[1]-x-8:
        dy+=kern+2
        dx=0
    
  return

# eop

