import struct
import serial
import math
import numpy
import time
import ev3

MBPORT = "/dev/tty.usbmodemFD122"
EVPORT = "/dev/tty.EV3-SerialPort"
BAUD = 115200

s = serial.Serial(MBPORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

evie = ev3.EV3(protocol = ev3.BLUETOOTH, host = EVPORT)
wallee = ev3.TwoWheelVehicle(ev3_obj = evie)
wallee.port_left = ev3.port.B
wallee.port_right = ev3.port.C

st = time.time()
aspeed = .4
fwd = 0
rot = 0

def clamp(t,a,b):
    return max(a,min(t,b))

ops_clear = b''.join([
    ev3.op.Input.Device,
    ev3.cmds.clr.CHANGES,
    ev3.LCX(0),
    ev3.LCX(0)
])

evie.send_direct_cmd(ops_clear)

ops_read = b''.join([
    ev3.op.Input.Device,
    ev3.cmds.Ready.SI,
    ev3.LCX(0),
    ev3.LCX(0),
    ev3.LCX(16),
    ev3.LCX(0),
    ev3.LCX(1),
    ev3.GVX(0)
])

ops_open = b''.join([
    ev3.op.Output.Speed,
    ev3.LCX(0),
    ev3.LCX(ev3.port.A),
    ev3.LCX(-50),
    ev3.op.Output.Start,
    ev3.LCX(0),
    ev3.LCX(ev3.port.A)
])

ops_close = b''.join([
    ev3.op.Output.Speed,
    ev3.LCX(0),
    ev3.LCX(ev3.port.A),
    ev3.LCX(50),
    ev3.op.Output.Start,
    ev3.LCX(0),
    ev3.LCX(ev3.port.A)
])

ops_stop = b''.join([
    ev3.op.Output.Stop,
    ev3.LCX(0),
    ev3.LCX(ev3.port.A),
    ev3.LCX(1)
])

def isTouching():
    reply = evie.send_direct_cmd(ops_read, global_mem=4)
    touched = int(struct.unpack('<f', reply[3:])[0])
    if touched == 1:
        return True
    else:
        return False

claw = False

try:
    while True:
        #read a line from the microbit, decode it and
        # strip the whitespace at the end
        data = s.readline().decode("ascii").rstrip()
        if data == 'None':
            continue
        #split the accelerometer data into x, y, z, a, b
        data_s = data.split(":")
        a = data_s[3]
        b = data_s[4]

        if claw:
            if a == 'False' and b == 'False':
                evie.send_direct_cmd(ops_stop)
                claw = False
            continue
        
        if a == 'True':
            evie.send_direct_cmd(ops_open)
            claw = True
            continue
        if b == 'True':
            evie.send_direct_cmd(ops_close)
            claw = True
            continue
        
        dt = time.time() - st
        st = time.time()
        g = numpy.array([float(i) for i in data_s[0:3]])
        rot = clamp(int(g[0]/16),-200,200)
        fwd = clamp(-int(g[1]/16),-100,100)
        if (abs(rot) < 10):
            rot = 0
        if (abs(fwd) < 10):
            fwd = 0
        if abs(rot) > abs(fwd):
            fwd = abs(rot)
            rot = int(math.copysign(200,rot))
        else:
            rot = 0
        wallee.move(speed = fwd, turn = rot)

        if a == 'True':
            pass
        if b == 'True':
            pass

finally:
    evie.send_direct_cmd(ops_stop)
    wallee.stop()
    s.close()
