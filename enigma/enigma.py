from microbit import *

wheels=[
{
  'forward': [9,14,4,18,10,15,6,-2,16,7,-9,-7,1,-6,11,2,-13,-7,-18,-1,3,-10,-14,-21,-5,-3],
  'reverse': [18,9,21,13,7,2,-4,6,14,-9,7,10,-6,-1,-10,-14,-7,-2,1,5,-15,-18,3,-3,-16,-11],
  'offset': 0
},
{
   'forward': [13,24,7,4,2,12,-4,16,4,15,8,11,-11,1,6,-10,-16,-9,3,-8,-5,-17,-12,-7,-21,-6],
   'reverse': [16,11,4,21,17,10,-2,-4,9,-7,12,8,-4,-13,-1,5,7,-12,-8,6,-6,-3,-11,-16,-15,-24],
   'offset': 0
},
{
   'forward': [5,9,14,4,15,6,17,7,-6,-8,-1,7,3,-10,11,2,-16,-5,-14,3,-7,-13,-2,1,-18,-4],
   'reverse': [16,8,6,10,14,-5,18,-4,13,1,-9,-6,5,7,-7,-3,-14,-2,-7,-15,2,4,-3,-17,-1,-11],
   'offset': 0
}
]

reflector = [4,12,8,13,-4,15,18,15,1,-1,-8,3,3,-12,-3,-3,-13,6,7,2,-15,-2,-15,-6,-18,-7]
pinboard = [23,23,5,22,1,-1,6,-5,7,0,0,0,-6,3,3,-7,-3,-3,4,0,0,0,-4,-23,-23,-22]

def brian (w,l,d):
    return l+wheels[w][d][(l+wheels[w]['offset'])%26]
def billy(a):
    return ord(a.upper())-65
def bob(a):
    return chr(a%26+65)
def ben(a):
    return a+reflector[a%26]
def bernard(a):
    return a+pinboard[a%26]
def barnaby(a):
    d=billy (a)
    o=bernard(d)
    n=brian(0,o,'forward')
    i=brian(1,n,'forward')
    e=brian(2,i,'forward')
    l=ben(e)
    m=brian(2,l,'reverse')
    u=brian(1,m,'reverse')
    f=brian(0,u,'reverse')
    t=bernard(f)
    y=bob(t)
    wheels[0]['offset']+=1
    wheels[1]['offset']+=1
    wheels[2]['offset']+=1
    return y

pins = [pin12,pin13,pin14,pin15,pin16]
val = 0
char = ""

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
        if char != "":
            display.clear()
            sleep(500)
            display.show(barnaby(char))
            char = ""

#while True:
#    if uart.any():
#        data = uart.readall()
#        char = chr(int.from_bytes(data,'big'))
#        display.show(barnaby(char))
