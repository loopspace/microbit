import radio
from microbit import *

DELAY=100
# Choose a unique name per microbit
#NAME="Niphredil"
NAME="Alfirin"
radio.on()

while True:
    sleep(DELAY)
    x,y,z = accelerometer.get_x(),accelerometer.get_y(),accelerometer.get_z()
    #
    # Experiments show that the ranges are:
    #
    # x [-2032,2048]
    # y [-2032,2048]
    # z [-2048,2032]
    #
    # The values for x and y need reversing to better fit into byte encoding
    # 
    x *= -1
    y *= -1
    #
    # Each is 8-bit, meaning that we can shift by 4 without losing precision
    #
    x >>= 4
    y >>= 4
    z >>= 4
    #
    # Convert to 2s complement
    #
    x %= 256
    y %= 256
    z %= 256
    #
    # Encode the button presses
    #
    if button_a.is_pressed():
        a = 1
    else:
        a = 0
    if button_b.is_pressed():
        b = 1
    else:
        b = 0
    #
    # Encode into a single integer
    #
    x <<= 18
    y <<= 10
    z <<= 2
    a <<= 1
    v = hex(x + y + z + a + b)[2:]
    #
    # v has length 7 characters
    #
    radio.send(v + ':' + NAME)
