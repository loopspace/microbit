#! python3

# http://ev3directcommands.blogspot.co.uk/

import ev3
import time

my_ev3 = ev3.EV3(protocol = ev3.TEST, host = '/dev/tty.EV3-SerialPort')
ev3_car = ev3.TwoWheelVehicle(ev3_obj = my_ev3)
my_ev3.sync_mode = ev3.SYNC
my_ev3.verbosity = 1
ev3_car.move(50,0)

ops = b''.join([
    ev3.op.Sound.Play,
    ev3.sound.TONE,
    ev3.LCX(1),
    ev3.LCX(262),
    ev3.LCX(500),
    ev3.op.Sound.Ready,
    ev3.op.Sound.Play,
    ev3.sound.TONE,
    ev3.LCX(1),
    ev3.LCX(330),
    ev3.LCX(500),
    ev3.op.Sound.Ready,
    ev3.op.Sound.Play,
    ev3.sound.TONE,
    ev3.LCX(1),
    ev3.LCX(392),
    ev3.LCX(500),
    ev3.op.Sound.Ready,
    ev3.op.Sound.Play,
    ev3.sound.TONE,
    ev3.LCX(2),
    ev3.LCX(523),
    ev3.LCX(1000)
])
my_ev3.send_direct_cmd(ops)
