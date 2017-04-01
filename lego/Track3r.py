#! /usr/bin/python3
import mbhandler
import ev3dev.ev3 as ev3

mbhandler.init()

# Left
mB = ev3.LargeMotor('outB')
# Right
mC = ev3.LargeMotor('outC')
# Arm
mA = ev3.MediumMotor('outA')

# Turn off all Leds to save power
ev3.Leds.all_off()

# Put arm in up position initially
mA.run_to_abs_pos(position_sp=0,speed_sp=100)
arm = False

def closedown():
    print("Closing down ... ")
    mbhandler.quit()
    ev3.Leds.all_off()
    mA.stop()
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
            spC = fwd*5
            spB = fwd*5
        mB.run_forever(speed_sp=spB)
        mC.run_forever(speed_sp=spC)
        if mb['button_a']['down']:
            if arm:
                mA.run_to_abs_pos(position_sp=0,speed_sp=100)
                arm = False
            else:
                mA.run_to_abs_pos(position_sp=178,speed_sp=100)
                arm = True
except KeyboardInterrupt:
    pass
finally:
    closedown()
