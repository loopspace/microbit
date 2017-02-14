import radio
from microbit import *

radio.on()
DELAY=50
state = { 'a': False, 'b': False }
motors = { 'l': 0, 'r': 0 }

def donum(i):
    print(i)
    pin1.write_digital(1)
    sleep(DELAY)
    for j in range(10):
        if i & 1 == 1:
            pin1.write_digital(1)
        else:
            pin1.write_digital(0)
        i >>= 1
        sleep(DELAY)
    pin1.write_digital(0)
            

pin1.write_digital(0)
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
    
    donum(2*l+r)

