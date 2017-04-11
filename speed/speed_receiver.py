import radio
from microbit import *

DELAY=100
radio.on()

while True:
    sleep(DELAY)
    msg = radio.receive()
    if msg == "Niphredil":
        print("A")
    elif msg == "Alfirin":
        print("B")
        
