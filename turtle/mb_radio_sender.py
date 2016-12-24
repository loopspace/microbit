import radio
from microbit import *

DELAY=100

radio.on()

while True:
    sleep(DELAY)
    x,y,z = accelerometer.get_x(),accelerometer.get_y(),accelerometer.get_z()
    a,b = button_a.was_pressed(),button_b.was_pressed()
    msg = str(x) + ':' + str(y) + ':' + str(z) + ':' + str(a) + ':' + str(b)
    radio.send(msg)
