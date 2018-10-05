from microbit import *
from neopixel import NeoPixel
import radio

# Set the queue length to 1 to ensure that the next message is the most recent
radio.on()
DELAY=50
MSGLEN=2
state = { 'a': False, 'b': False }

np = NeoPixel(pin0,5)
np.clear()

pin1.set_analog_period_microseconds(3000)
pin2.set_analog_period_microseconds(3000)

_fwd = 255
_bck = 767
_off = 511

def forward():
    pin1.write_analog(_fwd)
    pin2.write_analog(_bck)

def backward():
    pin1.write_analog(_bck)
    pin2.write_analog(_fwd)

def right():
    pin1.write_analog(_fwd)
    pin2.write_analog(_fwd)

def left():
    pin1.write_analog(_bck)
    pin2.write_analog(_bck)

def stop():
    pin1.write_analog(0)
    pin2.write_analog(0)

def getMessage():
    data = radio.receive()
    if data == 'None':
        return False
    if type(data) is not str:
        return False
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

    name = data.split(':')[1]
    e = {
        'name': name,
        'accelerometer': {
            'x': x,
            'y': y,
            'z': z,
        },
        'button_a': {
            'pressed': a,
            'down': a and not state['a'],
            'up': not a and state['a']
        },
        'button_b': {
            'pressed': b,
            'down': b and not state['b'],
            'up': not b and state['b']
        }
    }
    state['a'] = a
    state['b'] = b

    return e

    

while True:

    msg = getMessage()
    if msg:
        rot = msg['accelerometer']['x']
        fwd = msg['accelerometer']['y']
        if abs(rot) < 10:
            rot = 0
        if abs(fwd) < 10:
            fwd = 0
        if abs(rot) > abs(fwd):
            if rot > 0:
                left()
                np[4] = (0,0,0)
                np[0] = (63,63,0)
                np.show()
            else:
                right()
                np[0] = (0,0,0)
                np[4] = (63,63,0)
                np.show()
            display.show(Image.CONFUSED)
        elif abs(fwd) > abs(rot):
            if fwd > 0:
                backward()
                np[0] = (127,0,0)
                np[4] = (127,0,0)
                np.show()
                display.show(Image.TORTOISE)
            else:
                forward()
                np[0] = (42,42,42)
                np[4] = (42,42,42)
                np.show()
                display.show(Image.SURPRISED)
        else:
            stop()
            np.clear()
            display.show(Image.ASLEEP)
                
