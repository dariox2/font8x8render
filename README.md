
##font8x8render

Simple utility for annotating images, using 8x8 bitmap font

Author: Dario Albertocchi
License: Public Domain

```
import font8x8render

text=datetime.date.today().strftime("%Y-%m-%d")+" "+datetime.datetime.now().time().strftime("%H:%M:%S")

font8x8render.annotate_img(img, text,
                           x=50, # start 50 pixels from the left
                           y=-50, # minus, start 50 pixels from bottom
                           color=[128,255,128], # rgb light green
                           alpha=0.6, # transparency (default 1.0)
                           box="black") # add background (default none)
```


![Anu with timestamp](https://raw.githubusercontent.com/dariox2/font8x8render/master/demo_annotated.png)


See included example demo_img.py for more details.


A console renderer is also included to check 
the font; it takes character code as input:

```
python render.py 65 97 49

  XX
 XXXX
XX  XX
XX  XX
XXXXXX
XX  XX
XX  XX



 XXXX
    XX
 XXXXX
XX  XX
 XXX XX

  XX
 XXX
  XX
  XX
  XX
  XX
XXXXXX
```



###Credits

Based on the C version found at https://github.com/dhepper/font8x8
by Daniel Hepper <daniel@hepper.net>

These header files are directly derived from an assembler file fetched from:
http://dimensionalrift.homelinux.net/combuster/mos3/?p=viewsource&file=/modules/gfx/font8_8.asm

Original header:

; Summary: font8_8.asm
; 8x8 monochrome bitmap fonts for rendering
;
; Author:
;     Marcel Sondaar
;     International Business Machines (public domain VGA fonts)
;
; License:
;     Public Domain
;


