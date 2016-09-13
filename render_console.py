
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
    print(pr)
  
    
i=1

expr=""
for index, elem in enumerate(sys.argv):
  if index>0:
    ord = int(elem)
    bitmap = font8x8.select_set(ord)
    render(bitmap)

#eop

