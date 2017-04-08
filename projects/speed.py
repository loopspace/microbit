import radio
from microbit import *

DELAY = 100
NAME = "Niphredil"
#NAME = "Alfirin"
radio.on()

while True:
    sleep(DELAY)
    if button_a.was_pressed():
        radio.send(NAME)
        display.show([Image.DIAMOND_SMALL,Image.DIAMOND],wait=True,clear=True)
