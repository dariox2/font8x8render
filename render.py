
#
# Python version: Dario Albertocchi, 2016-09-12 (Programmer's Day)
#

import sys

import font8x8

def render(bitmap):
  x=0
  y=0
  setc=0
  mask=0
  for x in range(0,8):
    pr=""
    for y in range(0,8):
      setc = bitmap[x] & 1 << y
      if setc!=0:
        pr=pr+"X"
      else:
        pr=pr+" "
    print pr


def select_set(ord):
  if ord>=0 and ord<=127:
    bitmap=font8x8.font8x8_basic[ord]
  elif ord>=160 and ord<=255:
    bitmap=font8x8.font8x8_ext_latin[ord-160]
  else:
    bitmap=font8x8.font8x8_basic[32]
    
  return bitmap
  
    
i=1

expr=""
for index, elem in enumerate(sys.argv):
  if index>0:
    ord = int(elem)
    bitmap = select_set(ord)
    render(bitmap)

#eop

