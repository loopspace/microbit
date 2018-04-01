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

class Ball:

    def __init__(self,a,c):
        self.angle = a
        self.velocity = 0
        self.colour = c
        self.active = True

    def draw(self,clrs):
        a = (6 + math.floor( (self.angle/(2*math.pi) %1)*num_pixels))%num_pixels
        if self.active:
            clrs[a] = addTuple( self.colour, clrs[a] )
        else:
            clrs[a] = (127,127,127)

    def update(self,g,dt):
        if not self.active:
            return
        self.oangle = self.angle
        a = -g[0]/1024 * math.sin(self.angle) + g[1]/1024 * math.cos(self.angle)
        a -= friction * self.velocity
        self.angle += speed * self.velocity * dt
        self.angle %= 2*math.pi
        self.velocity += a * dt

    def collision(self,b):
        if not self.active or not b.active:
            return
        if s1dist(self.angle, b.angle) < math.pi/2:
            d = direction(self.angle, b.angle)
            od = direction(self.oangle, b.oangle)
            if d != od:
                if self.colour == b.colour:
                    self.active = False
                    b.active = False
                self.angle, b.angle = b.angle, self.angle
                self.velocity, b.velocity = b.velocity, self.velocity


np = neopixel.NeoPixel(pin0, num_pixels)
np.clear()

colours = [
    (127,0,0),
    (0,127,0),
    (0,0,127)
]

balls = []
balls.append( Ball(0, (127,0,0) ) )
balls.append( Ball(2*math.pi/3, (0,127,0) ) )
balls.append( Ball(4*math.pi/3, (0,0,127) ) )

et = running_time()
st = running_time()

while True:
    clrs = []
    for i in range(24):
        clrs.append( (0,0,0) )
    dt = (running_time() - et)/1000
    et = running_time()
    g = accelerometer.get_values()

    for i in range(len(balls)-1,-1,-1):
        if not balls[i].active:
            del balls[i]

    if et - st > spawn:
        i = random.randint(0,len(balls)-1)
        balls.insert(i, Ball( balls[(i-1)%(len(balls))].angle + s1diff(balls[(i-1)%(len(balls))].angle, balls[i].angle)/2,  random.choice(colours) ) )
        st = et
    
    for b in balls:
        b.update(g,dt)

    for i in range(len(balls)):
        balls[i].collision(balls[(i+1)%(len(balls))])

    for b in balls:
        b.draw(clrs)

    for i in range(24):
        np[i] = clrs[i]
    
    np.show()
