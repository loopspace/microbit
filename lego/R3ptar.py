#! /usr/bin/python3
import mbhandler
import ev3dev.ev3 as ev3

mbhandler.init()


# Steering
mA = ev3.MediumMotor('outA')
# Drive
mB = ev3.LargeMotor('outB')
# Head
mD = ev3.LargeMotor('outD')


def closedown():
    print("Closing down ...")
    mbhandler.quit()
    ev3.Leds.all_off()
    mA.stop()
    mB.stop()
    mD.stop()
    exit()

def strike():
    mD.stop_action = 'hold'
    strike_pos = -10
    mD.run_to_abs_pos(position_sp=strike_pos,speed_sp=50)
    mD.wait_while('running')
    mD.run_to_abs_pos(position_sp=-strike_pos,speed_sp=300)
    mD.wait_while('running')
    mD.run_to_abs_pos(position_sp=strike_pos,speed_sp=50)
    mD.wait_while('running')

def turnto(t):
    t = (t + 1)/2
    return 60*t -30*(1 - t)
    
try:
    while True:
        mb = mbhandler.queue.get()
        rot = mb['accelerometer']['x']
        fwd = mb['accelerometer']['y']
        if abs(rot) < 10:
            rot = 0
        if abs(fwd) < 10:
            fwd = 0
        if fwd != 0:
            mB.run_forever(speed_sp=fwd*5)
            mD.run_to_abs_pos(position_sp=turnto(rot),speed_sp=50)
        if mb['button_a']['down']:
            strike()
        
except KeyboardInterrupt:
    pass
finally:
    closedown()
    
