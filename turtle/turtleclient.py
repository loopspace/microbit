import serial
import math
import numpy
import time
import turtle

PORT = "/dev/tty.usbmodemFA132"
BAUD = 115200

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

wn = turtle.Screen()
mbit = turtle.Turtle()
mbit.left(90)

st = time.time()
aspeed = .4

colours = [
    '#ff0000',
    '#ffff00',
    '#00ff00',
    '#00ffff',
    '#0000ff',
    '#ff00ff'
]

mbitcolour = 0
mbit.pencolor(colours[mbitcolour])

try:
    while True:
        #read a line from the microbit, decode it and
        # strip the whitespace at the end
        data = s.readline().decode("ascii").rstrip()
        #split the accelerometer data into x, y, z, a, b
        data_s = data.split(" ")
        dt = time.time() - st
        st = time.time()
        g = numpy.array([float(i) for i in data_s[0:3]])
        a = data_s[3]
        b = data_s[4]
        rot = math.atan2(g[0],g[2])*180/math.pi*dt*aspeed
        fwd = math.atan2(-g[1],g[2])*180/math.pi*dt*aspeed
        mbit.left(rot)
        mbit.forward(fwd)

        if a == 'True':
            if mbit.isdown():
                mbit.penup()
            else:
                mbit.pendown()

        if b == 'True':
            mbitcolour += 1
            mbitcolour %= 6
            mbit.pencolor(colours[mbitcolour])


finally:
    s.close()

wn.mainloop()
