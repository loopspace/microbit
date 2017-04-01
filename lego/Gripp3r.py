#! /usr/bin/python3
import select
import sys
import serial
import ev3dev.ev3 as ev3

MBPORT = "/dev/ttyACM0"
BAUD = 115200

s = serial.Serial(MBPORT)
s.baudrate = BAUD
s.parity = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE
s.reset_input_buffer()

mB = ev3.LargeMotor('outB')
mC = ev3.LargeMotor('outC')
mA = ev3.MediumMotor('outA')
btn = ev3.Button()

claw = False


def closedown():
	print("Closing down ...")
	ev3.Sound.play('/home/robot/current/programs/microbit/leke.wav')
	s.close()
	ev3.Leds.all_off()
	mA.stop()
	mB.stop()
	mC.stop()
	exit()

def btnclose(b):
	closedown()

btn.on_backspace = btnclose

print("Ready to go ...")
ev3.Sound.play('/home/robot/current/programs/microbit/klar.wav')
try:
	while True:
		btn.process()
		data = s.readline().decode('ascii').rstrip()
		if data == 'None':
			continue
		data_s = data.split(":")
		if len(data_s) != 5:
			continue
		a = data_s[3]
		b = data_s[4]
	
		if claw:
			if a == 'False' and b == 'False':
				mA.stop()
				claw = False
			continue
	
		if a == 'True':
			ev3.Leds.set_color(ev3.Leds.LEFT,ev3.Leds.RED)
			ev3.Leds.set_color(ev3.Leds.RIGHT,ev3.Leds.RED)
			mA.run_forever(speed_sp=180)
			claw = True
			continue
		if b == 'True':
			ev3.Leds.set_color(ev3.Leds.LEFT,ev3.Leds.GREEN)
			ev3.Leds.set_color(ev3.Leds.RIGHT,ev3.Leds.GREEN)
			mA.run_forever(speed_sp=-180)
			claw = True
			continue
	
		rot = int(data_s[0])/16
		fwd = int(data_s[1])/16
		if abs(rot) < 10:
			rot = 0
		if abs(fwd) < 10:
			fwd = 0
		if abs(rot) > abs(fwd):
			spB = rot*5
			spC = -rot*5
		else:
			spB = -fwd*5
			spC = -fwd*5
		mB.run_forever(speed_sp=spB)
		mC.run_forever(speed_sp=spC)
except KeyboardInterrupt:
	pass	
finally:
	closedown()
