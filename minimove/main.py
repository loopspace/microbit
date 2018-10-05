from microbit import *
from neopixel import NeoPixel

np = NeoPixel(pin0,5)
np.clear()

pin1.set_analog_period_microseconds(3000)
pin2.set_analog_period_microseconds(3000)

fwd = 255
bck = 767
off = 511

state = 4

numactions = 4
action = 0

def forward(t):
    pin1.write_analog(fwd)
    pin2.write_analog(bck)
    sleep(t)
    pin1.write_digital(0)
    pin2.write_digital(0)

def backward(t):
    pin1.write_analog(bck)
    pin2.write_analog(fwd)
    sleep(t)
    pin1.write_digital(0)
    pin2.write_digital(0)

def right(t):
    pin1.write_analog(fwd)
    pin2.write_analog(fwd)
    sleep(t)
    pin1.write_digital(0)
    pin2.write_digital(0)

def left(t):
    pin1.write_analog(bck)
    pin2.write_analog(bck)
    sleep(t)
    pin1.write_digital(0)
    pin2.write_digital(0)



def doAction(n):
    n %= numactions
    left((n + 1) * 500)

while True:

    if accelerometer.get_y() < 800:
        if button_a.was_pressed():
            action += 1
            action %= numactions

        if button_b.was_pressed():
            action -= 1
            action %= numactions

        state = 0
        display.show(str(action))
    else:
        if state == 0:
            np.clear()
            lights = 0
            state = 1
            time = running_time()
        elif state == 1:
            display.show(Image.SURPRISED)
            lights = min(5,int((running_time() - time)/1000))
            for i in range(lights):
                np[i] = (255,0,0)
            np.show()
            if int( (running_time() - time)/1000 ) >= 6:
                np.clear()
                state = 2
        elif state == 2:
            display.show(Image.TORTOISE)
            doAction(action)
            state = 3
            time = running_time()
        elif state == 3:
            display.show(Image.CONFUSED)
            lights = min(5,int((running_time() - time)/1000))
            for i in range(lights):
                np[4 - i] = (0,0,255)
            np.show()
            if int( (running_time() - time)/1000 ) >= 6:
                np.clear()
                state = 4
        else:
            display.show(Image.ASLEEP)
