#! python3

# http://ev3directcommands.blogspot.co.uk/

import ev3
import time
import struct

my_ev3 = ev3.EV3(protocol = ev3.BLUETOOTH, host = '/dev/tty.EV3-SerialPort')
my_ev3.sync_mode = ev3.SYNC
my_ev3.verbosity = 0
ev3_car = ev3.TwoWheelVehicle(ev3_obj = my_ev3)
ev3_car.verbosity = 1
ev3_car.port_left = ev3.port.B
ev3_car.port_right = ev3.port.C
#ev3_car.move(50,0)
ev3_car.stop()

ops = b''.join([
    ev3.op.Com.Get,
    ev3.cmds.get.BRICKNAME,
    ev3.LCX(16),
    ev3.GVX(0)
])

ops_clear = b''.join([
    ev3.op.Input.Device,
    ev3.cmds.clr.CHANGES,
    ev3.LCX(0),
    ev3.LCX(0)
])

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

my_ev3.send_direct_cmd(ops_clear)

while True:
    reply = my_ev3.send_direct_cmd(ops_read, global_mem=4)
    touched = int(struct.unpack('<f', reply[3:])[0])
    if touched == 1:
        print("Touched")

