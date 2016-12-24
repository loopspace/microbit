import radio
from microbit import *

DELAY=100

radio.on()

while True:
    sleep(DELAY)
    msg = radio.receive()
    print(msg)
