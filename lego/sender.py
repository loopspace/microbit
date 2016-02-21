import time

commands = {
    'OUTPUT_RESET': 'A2',
    'OUTPUT_STOP': 'A3',
    'OUTPUT_POWER': 'A4', # seems to max out around 0x28
    'OUTPUT_SPEED': 'A5',
    'OUTPUT_START': 'A6',
    'OUTPUT_POLARITY': 'A7',
}

motors = {
    'A': 1,
    'B': 2,
    'C': 4,
    'D': 8
}

# command to start motor on port A at speed 20
# 0C 00 00 00 80 00 00 A4 00 01 14 A6 00 01
# 12  0  0  0 128 0  0 164 0  1 20 166 0  1
#
# Length: 0C 00 -> 12
# Counter: 00 00 -> 0
# Reply: 80 -> No reply
# Variables: 00 00 -> None (?)
# Command: A4 -> opOUTPUT_POWER
# 00: Null block
# Motor: 01 -> A
# Value: 14 -> 20
# Command: A6 -> opOUTPUT_START
# 00: Null block
# Motor: 01 -> A
#
start_motor_str = '0C000000800000A4000214A60002'
start_motor = bytes.fromhex(start_motor_str)

# command to stop motor on port A
# 09 00 01 00 80 00 00 A3 00 01 00
#  9  0  1  0 128 0  0 163 0  1  0
#
# Length: 09 00 -> 9
# Counter: 01 00 -> 1
# Reply: 80 -> No reply
# Variables: 00 00 -> None (?)
# Command: A3 -> opOUTPUT_STOP
# 00: Null block
# Motor: 01 -> A
# Value: 00 -> Float

stop_motor_str = '09000100800000A3000200'
stop_motor = bytes.fromhex(stop_motor_str)

# send commands to EV3 via bluetooth
with open('/dev/tty.EV3-SerialPort', 'wb', 0) as bt:
    bt.write(start_motor)
    time.sleep(1)
    bt.write(stop_motor)
