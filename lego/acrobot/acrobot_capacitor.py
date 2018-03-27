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
    pin1.write_analog(m*16)
    sleep(DELAY)

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
    if x > 127:
        x -= 256
    if y > 127:
        y -= 256
    if z > 127:
        z -= 256
    x *= -1
    y *= -1
    
    ad = a and not state['a']
    au = not a and state['a']
    bd = b and not state['b']
    bu = not b and state['b']
    state['a'] = a
    state['b'] = b

    if abs(x) < 10:
        x = 0
    if abs(y) < 10:
        y = 0
    if x == 0 and y == 0:
        continue
    
    l = 0
    r = 0
    if abs(x) > abs(y):
        if x > 0:
            l = 1
        else:
            r = 1
    else:
        if y > 0:
            l = 1
            r = 1
    if l == motors['l'] and r == motors['r']:
        continue
    motors['l'] = l
    motors['r'] = r
    
    setnum(2*l+r,(2*l+r)*16)

