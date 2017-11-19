from microbit import *

pins = [pin12,pin13,pin14,pin15,pin16]
val = 0

while True:
    tval = 0
    for i in range(5):
        tval *= 2
        if pins[i].read_digital():
            tval += 1
    if tval == 0:
        val = 0
    val |= tval
    if val > 0:
        char = chr(val+64)
        display.show(char)
    else:
        display.clear()
