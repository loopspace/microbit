from microbit import *
import neopixel
import math
import random

num_pixels = 24
friction = .05
speed = 1
spawn = 1000

def direction(a,b):
    if a == b or a == b + math.pi or a == b - math.pi:
        return 0
    if a < math.pi:
        if a < b and b < a + math.pi:
            return 1
        else:
            return -1
    if b < math.pi:
        if b < a and a < b + math.pi:
            return -1
        else:
            return 1
    if a < b:
        return 1
    else:
        return -1


def s1diff(a,b):
    if b < a:
        b += 2*math.pi
    return b - a
    
def s1dist(a,b):
    return min( abs( s1diff(a,b) ), abs( s1diff(b,a) ) )

def addTuple(a,b):
    return (min(a[0] + b[0],255),min(a[1] + b[1],255),min(a[2] + b[2],255))

np = neopixel.NeoPixel(pin0, num_pixels)
np.clear()

colours = [
    (127,0,0),
    (0,127,0),
    (0,0,127),
    (127,127,127)
]

balls = []
balls.append( [0,0,0] )
balls.append( [2*math.pi/3,0,1] )
balls.append( [4*math.pi/3,0,2] )

et = running_time()
st = running_time()

while True:
    clrs = []
    for i in range(24):
        clrs.append( (0,0,0) )
    dt = (running_time() - et)/1000
    et = running_time()
    gx = accelerometer.get_x()/1024
    gy = accelerometer.get_y()/1024

    if et - st > spawn:
        d = s1dist(balls[0][0], balls[ len(balls) - 1][0])
        k = 0
        for i in range(len(balls) - 1):
            if s1dist(balls[i][0], balls[i+1][0]) < d:
                k = i+1
                d = s1dist(balls[i][0], balls[i+1][0])
        balls.insert(k, [ (balls[k][0] + balls[ (k+1) % len(balls) ][0])/2, 0, random.randint(0,2) ] )
        st = et

    p = []
    for b in balls:
        p.append(b[0])
        a = -gx * math.sin(b[0]) + gy * math.cos(b[0]) - friction * b[1]
        b[0] += speed * b[1] * dt
        b[0] %= 2*math.pi
        b[1] += a * dt

    r = set()
    for i in range(len(balls)):
        j = (i+1)%(len(balls))
        if s1dist(balls[i][0], balls[j][0]) < math.pi/2 and direction(balls[i][0], balls[j][0]) != direction(p[i], p[j]):
            if balls[i][2] == balls[j][2]:
                balls[i][2] = 3
                balls[j][2] = 3
                r.add(i)
                r.add(j)
            else:
                balls[i][0], balls[j][0] = balls[j][0], balls[i][0]
                balls[i][1], balls[j][1] = balls[j][1], balls[i][1]

    for b in balls:
        a = (6 + math.floor( (b[0]/(2*math.pi) %1)*num_pixels))%num_pixels
        clrs[a] = addTuple( colours[b[2]], clrs[a] )

    r = sorted(list(r), reverse = True)

    for i in r:
        del balls[i]
        
    for i in range(24):
        np[i] = clrs[i]
    
    np.show()
