from microbit import *

while True:
    for j in range(-1,2,2):
        for i in range(5):
            display.set_pixel(2 + j * (i - 2),i,9)
            sleep(250)
            display.set_pixel(2 + j * (i - 2),i,0)
        for i in range(3):
            display.set_pixel(2 + 2*j,3-i,9)
            sleep(250)
            display.set_pixel(2 + 2*j,3-i,0)
