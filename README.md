
font8x8render
=============

Simple python program for annotate images using 8x8 bitmap font

Author: Dario Albertocchi
License: Public Domain

See included example demo_img.py 


A console renderer is also included to visualize
the font; it takes character code as input:

#python render.py 65 97 49

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



Credits
=======

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


