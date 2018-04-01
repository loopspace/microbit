from microbit import *
import neopixel
import math
#import random

num_pixels = 24
friction = .05
speed = 1
spawn = 1000

def direction(a,b):
    """Figure out the clockwise/anticlockwise direction."""
    # a and b are between 0 and 2 pi

    # Check if they are equal or opposite
    if a == b or a == b + math.pi or a == b - math.pi:
        return 0
    if a < math.pi:
        # a is in the first part
        # so if b is anticlockwise it must be between a and a + pi 
        if a < b and b < a + math.pi:
            # b is between a and a + pi, so b is anticlockwise from a
            return 1
        else:
            return -1
    if b < math.pi:
        # b is in the first part
        # so if a is anticlockwise, it must be between b and b + pi
        if b < a and a < b + math.pi:
            # a is anticlockwise of b, so b is clockwise of a
            return -1
        else:
            return 1
    # To get here, both are in pi to 2 pi, so a simple test is fine
    if a < b:
        return 1
    else:
        return -1


def s1diff(a,b):
    """Angle from a to b in an anticlockwise direction."""
    if b < a:
        b += 2*math.pi
    return b - a
    
def s1dist(a,b):
    """Angular distance between two angles."""
    return min( abs( s1diff(a,b) ), abs( s1diff(b,a) ) )


class Colour:

    def __init__(self,*args):
        if type(args[0]) == type((1,2)):
            self.r = args[0][0]
            self.g = args[0][1]
            self.b = args[0][2]
        elif type(args[0]) == type(""):
            if args[0] == "hsl":
                self.fromHsl(args[1],args[2],args[3])
            elif args[0] == "hsv":
                self.fromHsv(args[1],args[2],args[3])
        else:
            self.r = args[0]
            self.g = args[1]
            self.b = args[2]


    def __eq__(self,c):
        if self.r != c.r:
            return False
        if self.g != c.g:
            return False
        if self.b != c.b:
            return False
        return True
    
    def toTuple(self):
        return (self.r, self.g, self.b)

    def add(self,c):
        return Colour( min(self.r + c.r, 255), min(self.g + c.g, 255), min(self.b + c.b, 255) )

    def fromHsl(self,h,s,l):
        h = (h - math.floor(h)) * 6
        c = (1 - abs(2 * l - 1)) * s * 255
        m =  l * 255 - c/2
        x = c * (1 - abs(h%2 - 1))
        if h < 1:
            self.r,self.g,self.b = int(c + m), int(x + m), int(m)
        elif h < 2:
            self.r,self.g,self.b = int(x + m), int(c + m), int(m)
        elif h < 3:
            self.r,self.g,self.b = int(m), int(c + m), int(x + m)
        elif h < 4:
            self.r,self.g,self.b = int(m), int(x + m), int(c + m)
        elif h < 5:
            self.r,self.g,self.b = int(x + m), int(m), int(c + m)
        else:
            self.r,self.g,self.b = int(c + m), int(m), int(x + m)


    def fromHsv(self,h,s,v):
        h = (h - math.floor(h)) * 6
        m = (v - s*v)*255 
        c = s * v * 255 
        x = c * (1 - abs(h%2 - 1)) 
        if h < 1:
            self.r,self.g,self.b = int(c+m),int(x+m),int(m)
        elif h < 2:
            self.r,self.g,self.b = int(x+m),int(c+m),int(m)
        elif h < 3:
            self.r,self.g,self.b = int(m),int(c+m),int(x+m)
        elif h < 4:
            self.r,self.g,self.b = int(m),int(x+m),int(c+m)
        elif h < 5:
            self.r,self.g,self.b = int(x+m),int(m),int(c+m)
        else:
            self.r,self.g,self.b = int(c+m),int(m),int(x+m)


    
class Ball:

    def __init__(self,a,c):
        """Initialise the ball with a position and colour."""
        self.angle = a
        self.velocity = 0
        self.colour = Colour( c )
        self.active = True

    def draw(self,clrs):
        """Draw a pixel at the right position."""
        a = (6 + math.floor( (self.angle/(2*math.pi) %1)*num_pixels))%num_pixels
        if self.active:
            clrs[a] = self.colour.add( clrs[a] )
        else:
            clrs[a] = Colour(255,255,255)


    def update(self,g,dt):
        """Update the position and velocity given the gravity and delta time."""
        if not self.active:
            return
        self.oangle = self.angle
        a = -g[0]/1024 * math.sin(self.angle) + g[1]/1024 * math.cos(self.angle)
        a -= friction * self.velocity
        self.angle += speed * self.velocity * dt
        self.angle %= 2*math.pi
        self.velocity += a * dt

    def collision(self,b):
        """Decide whether this ball has collided with ball b and update accordingly."""
        if not self.active or not b.active:
            return
        # Check if distance is less than a quarter circle
        if s1dist(self.angle, b.angle) < math.pi/2:
            d = direction(self.angle, b.angle)
            od = direction(self.oangle, b.oangle)
            if d != od:
                # Directions have changed, collision
                self.angle, b.angle = b.angle, self.angle
                self.velocity, b.velocity = b.velocity, self.velocity


display.show("Initialising")


display.show("Finishing")
