from microbit import *
import neopixel

num_of_pix = 24
np = neopixel.NeoPixel(pin0, num_of_pix) # create a NeoPixel object on pin0

p = 0 # set pixel pointer to 0
while True:
    np.clear()
    np[p] = (0,0,60) # set the RGB values to be blue (red=0, green=0, blue=60)
    np.show()
    sleep(7)

        # if p is at the 24th ZIP LED, go back to 0 (back to the the start of the circle)
    if p < 23:
        p += 1
    else:
        p = 0
