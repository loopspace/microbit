from microbit import *

DELAY=100

while True:
    sleep(DELAY)
    x,y,z = accelerometer.get_x(),accelerometer.get_y(),accelerometer.get_z()
    a,b = button_a.was_pressed(),button_b.was_pressed()
    print(x,y,z,a,b)