#
# Render text with 8x8 font over an image
#
# Author: Dario Albertocchi, 2016-09-12 (Programmer's Day)
# License: Public Domain
#
# Notes: parameters follow screen convention (x=horiz, y=vert),
#        which is inverted with respect arrays.
#        this is a mess. don't judge me. :p
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

  if x>=0 and x<img.shape[0] and y>=0 and y<img.shape[1]:
    img[x, y] = newcol(img[x, y], color, alpha)

  return


def annotate_img(img, text, x=8, y=8, dir="horiz", 
	color=[128,128,128], alpha=1.0, zoom=1, box="none"):

  kern=8

  vert=(dir=="vert")

  if x<0:
    x=img.shape[1]+x
  if y<0:
    y=img.shape[0]+y
  

  # warn, see note above
  xmin,xmax=y,y
  ymin,ymax=x,x
  maxline=1

  if box=="white":
    bgcol=[255,255,255]
  elif box=="black":
    bgcol=[0,0,0]
  else:
    bgcol=[128,128,128]

  dx=0
  dy=0
  currline=1
  i=0
  while i<len(text):

    ucod=ord(text[i:i+1])
      
    # ignore spaces at line beginning 
    if ucod==32 and ((dx==0 and not vert) or (dy==0 and vert)):
      text=text[0:i]+text[i+1:]
      continue

    bitmap = select_set(ucod)

    # Draw a character
    for py in range(0, 8 if vert else 9 ):
      for px in range(0, 9 if vert else 8):
        if py>=0 and py<8 and px>=0 and px<8:
          if vert:
            pixel = bitmap[7-px] & 1 << py
          else:
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

    if vert:
      dy+=kern*zoom
      if y+dy+kern*zoom>=img.shape[0]-kern*zoom/2:
        dx-=(kern+1)*zoom
        dy=0
        maxline=currline
        currline=1
      else:
        currline+=1
    else:
      dx+=kern*zoom
      if x+dx+kern*zoom>=img.shape[1]-kern*zoom/2:
        dy+=(kern+1)*zoom
        dx=0
        maxline=currline
        currline=1
      else:
        currline+=1

    # aesthetic: match longest line length
    while (len(text) % maxline) != 0:
      text=text+" "

    i+=1

  
  # draw a border to improve appearence of background 
  if box!="none":
    l=xmin-2*zoom
    r=xmax+2*zoom
    t=ymin-2*zoom
    b=ymax+2*zoom
    for i in range(l, r):
      for j in range(t, b):
        if (i<l+2*zoom or i>r-2*zoom) or \
           (j<t+2*zoom or j>b-2*zoom):
          putpix(img, i, j, bgcol, alpha)


  return

# eop

