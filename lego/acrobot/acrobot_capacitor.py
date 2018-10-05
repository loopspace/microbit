import radio
from microbit import *

# Set the queue length to 1 to ensure that the next message is the most recent
radio.on()
#radio.config(queue=1)
state = { 'a': False, 'b': False }
motors = { 'l': 0, 'r': 0 }
pin1.write_digital(0)

# Capacitor: 3.3uF, Resistor: 15kO (I think, could be 10kO)
# Signal resolution: 16, corresponds to about 5 on the RCX

DELAY=1000

def setnum(n,m):
#    display.show(str(n))
    pin1.write_analog(m)
#    sleep(DELAY)

pin1.set_analog_period(1)

while True:
    data = radio.receive()
    if data == 'None':
        continue
    if type(data) is not str:
        continue
    v = int(data.split(':')[0],16)
    b = (v & 1 == 1)
    v >>= 1
    a = (v & 1 == 1)
    v >>= 1
    z = v & 255
    v >>= 8
    y = v & 255
    v >>= 8
    x = v & 255

    y >>= 4

    y -= (y & 8)*2 - 8
    
    setnum(y,y*64)

