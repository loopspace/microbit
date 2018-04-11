from microbit import *
import neopixel
import math
import random

num_pixels = 24
friction = .05
speed = 1
position = 0
velocity = 0
fadeFactor = .9

np = neopixel.NeoPixel(pin0, num_pixels)
np.clear()

et = running_time()
st = running_time()

generate = running_time() + random.randint(2000,4000)
lifetime = running_time()
hasTarget = False
score = 0
gameOver = False

def fade(t):
    return math.floor(t*fadeFactor)

while True:
    if gameOver:
        if button_a.was_pressed():
            score = 0
            hasTarget = False
            generate = running_time() + random.randint(2000,4000)
            lifetime = running_time()
            st = running_time()
            gameOver = False
            position = 0
            velocity = 0
            display.clear()
        else:
            continue
            
    for i in range(num_pixels):
        np[i] = tuple(map(fade,np[i]))

    if running_time() > generate:
        target = random.randint(0,num_pixels-1)
        lifetime = random.randint(3000,6000) + running_time()
        generate = lifetime + random.randint(2000,4000)
        lives = random.randint(0,1)*2 - 1
        hasTarget = True

    if running_time() > lifetime:
        hasTarget = False
        
    if hasTarget:
        if lives == 1:
            np[target] = (np[target][0],255,np[target][2])
        else:
            np[target] = (255,np[target][1],np[target][2])
            
    gx = accelerometer.get_x()/1024
    gy = accelerometer.get_y()/1024
    dt = (running_time() - et)/1000
    et = running_time()
    a = -gx * math.sin(position) + gy * math.cos(position) - friction * velocity
    position += speed * velocity * dt
    position %= 2*math.pi
    velocity += a * dt

    a = (6 + math.floor( (position/(2*math.pi) %1)*num_pixels))%num_pixels
    np[a] = (0,0,255)

    if hasTarget and a == target:
        np[a] = (255,255,255)
        score += lives
        if score > 0:
            if lives == 1:
                display.set_pixel((score-1)%5,math.floor(((score-1)/5)%5),9)
            else:
                display.set_pixel(score%5,math.floor((score/5)%5),0)
        else:
            gameOver = True
            display.show(str(math.floor((running_time() - st)/1000)))
            np.clear()
                
        hasTarget = False
        generate = running_time() + random.randint(2000,4000)

    
    np.show()
    
