#! /usr/bin/python3

import mbhandler
import ev3dev.ev3 as ev3

mbhandler.init()

mB = ev3.LargeMotor('outB')
mC = ev3.LargeMotor('outC')

def closedown():
    print("Closing down ...")
    mbhandler.quit()
    ev3.Leds.all_off()
    mB.stop()
    mC.stop()
    exit()

try:
    while True:
        mb = mbhandler.queue.get()
        rot = mb['accelerometer']['x']
        fwd = mb['accelerometer']['y']
        if abs(rot) < 10:
            rot = 0
        if abs(fwd) < 10:
            fwd = 0
        if abs(rot) > abs(fwd):
            spB = rot*5
            spC = -rot*5
        else:
            spB = fwd*5
            spC = fwd*5
        mB.run_forever(speed_sp=spB)
        mC.run_forever(speed_sp=spC)

except KeyboardInterrupt:
    pass
finally:
    closedown()
