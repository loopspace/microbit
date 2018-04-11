from microbit import *
import neopixel
import math

num_pixels = 24
np = neopixel.NeoPixel(pin0, num_pixels)
np.clear()

while True:
    gx = accelerometer.get_x()/1024
    gy = accelerometer.get_y()/1024

    a = math.floor(math.atan2(gy,gx)/math.pi*12 - 5.5)%num_pixels

    np.clear()
    np[a] = (255,255,255)
    np[(a+6)%num_pixels] = (255,0,0)
    np[(a+12)%num_pixels] = (0,255,0)
    np[(a+18)%num_pixels] = (0,0,255)
    np.show()
    
