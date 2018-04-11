from microbit import *
import neopixel
import math

num_pixels = 24
friction = .05
speed = 1
position = 0
velocity = 0
fadeFactor = .9

np = neopixel.NeoPixel(pin0, num_pixels)
np.clear()

et = running_time()

def fade(t):
    return math.floor(t*fadeFactor)

while True:
    for i in range(num_pixels):
        np[i] = tuple(map(fade,np[i]))

    gx = accelerometer.get_x()/1024
    gy = accelerometer.get_y()/1024
    dt = (running_time() - et)/1000
    et = running_time()
    a = -gx * math.sin(position) + gy * math.cos(position) - friction * velocity
    position += speed * velocity * dt
    position %= 2*math.pi
    velocity += a * dt

    a = (6 + math.floor( (position/(2*math.pi) %1)*num_pixels))%num_pixels
    np[a] = (0,0,255)
    np.show()
    
