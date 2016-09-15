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


def putpix(img, x, y, color, alpha):

  img[x, y] = newcol(img[x, y], color, alpha)

  return


def annotate_img(img, text, x=8, y=8, dir="horiz", 
	color=[128,128,128], alpha=1.0, zoom=1, box="none"):

  kern=8

  if y=="bottom":
  	y=img.shape[0]-(kern*zoom*2)

  xmin=x
  ymin=y
  xmax=x
  ymax=y

  if box=="white":
    bgcol=[255,255,255]
  elif box=="black":
    bgcol=[0,0,0]
  else:
    bgcol=[128,128,128]

  dx=0
  dy=0
  for i in range(0, len(text)):

    c=text[i:i+1]
    bitmap = select_set(ord(c))

    # Draw a character
    for py in range(0, 8):
      for px in range(0, 8):
        if py>=0 and py<8 and px>=0 and px<8:
          pixel = bitmap[py] & 1 << px
        else:
          pixel=0
          
        for zy in range(0, zoom):
          for zx in range(0, zoom):

            xpos=y+dy+py*zoom+zy
            ypos=x+dx+px*zoom+zx

            xmin=min(xmin,xpos)
            ymin=min(ymin,ypos)
            xmax=max(xmax,xpos)
            ymax=max(ymax,ypos)

            if pixel != 0:
              putpix(img, xpos, ypos, color, alpha)
            elif box != "none":
              putpix(img, xpos, ypos, bgcol, alpha)

    if dir=="vert":
      dy+=(kern+1)*zoom
      if y+dy+kern*zoom>=img.shape[0]:
        dx+=(kern+1)*zoom
        if x+dx+kern*zoom>=img.shape[1]:
          return
        dy=0
    else:
      dx+=kern*zoom
      if x+dx+kern*zoom>=img.shape[1]:
        dy+=(kern+2)*zoom
        if y+dy+kern*zoom>=img.shape[0]:
          return
        dx=0
    
  if box!="none":
    for i in range(xmin,xmax):
      putpix(img, i, ymin-2, bgcol, alpha)
    #for i in range(ymin,ymax):
    #  print(i)
    #  putpix(img, i, xmin-1, bgcol, alpha)


  return

# eop

