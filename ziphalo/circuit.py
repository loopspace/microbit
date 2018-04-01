from microbit import *
from random import randint
import neopixel

import math

def hsl2rgb(h,s,l):
    h = (h - math.floor(h)) * 6
    c = (1 - abs(2 * l - 1)) * s * 255
    m =  l * 255 - c/2
    x = c * (1 - abs(h%2 - 1))
    if h < 1:
        return int(c + m), int(x + m), int(m)
    elif h < 2:
        return int(x + m), int(c + m), int(m)
    elif h < 3:
        return int(m), int(c + m), int(x + m)
    elif h < 4:
        return int(m), int(x + m), int(c + m)
    elif h < 5:
        return int(x + m), int(m), int(c + m)
    else:
        return int(c + m), int(m), int(x + m)


def hsv2rgb(h,s,v):
    h = (h - math.floor(h)) * 6
    m = (v - s*v)*255 
    c = s * v * 255 
    x = c * (1 - abs(h%2 - 1)) 
    if h < 1:
        return int(c+m),int(x+m),int(m)
    elif h < 2:
        return int(x+m),int(c+m),int(m)
    elif h < 3:
        return int(m),int(c+m),int(x+m)
    elif h < 4:
        return int(m),int(x+m),int(c+m)
    elif h < 5:
        return int(x+m),int(m),int(c+m)
    else:
        return int(c+m),int(m),int(x+m)


num_of_pix = 24
np = neopixel.NeoPixel(pin0, num_of_pix) # create a NeoPixel object on pin0

p = 0 # set pixel pointer to 0
h = 0
r,g,b = hsl2rgb(0,1,.25)
while True:
#    np.clear()

    np[p] = (0,0,0)
    np[-p] = (0,0,0)

    p += 1
    if p == 24:
        p = 0
        h += 1
        r,g,b = hsl2rgb(h/24,1,.25)

    np[p] = (r,g,b)
    np[-p] = (r,g,b)

    np.show()
    sleep(70)

    # if p is at the 24th ZIP LED, go back to 0 (back to the the start of the circle)
