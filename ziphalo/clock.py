from microbit import *
import neopixel
import math

num_pixels = 24
np = neopixel.NeoPixel(pin0, num_pixels)
np.clear()

running = False
st = running_time()
et = running_time()

stepTime = num_pixels/1000

intensity = 127

red = 0
green = 0
blue = 0

shiftG = False
shiftB = False

while True:
    clrs = []
    for i in range(24):
        clrs.append( (0,0,0) )

    if button_a.was_pressed():
        if running:
            running = False
            et = str((running_time() - st)/1000)
            display.show(et)
        else:
            running = True
            display.clear()
            et = running_time()
            red = 0
            green = 0
            blue = 0

    if button_b.was_pressed() and not running:
        display.show(et)
        
    if running and running_time() - et > stepTime:
        et = et + stepTime
        red += 1
        red %= num_pixels

        if red == green:
            if shiftG:
                if green == blue:
                    if shiftB:
                        blue += 1
                        blue %= num_pixels
                        shiftB = False
                else:
                    shiftB = True
                green += 1
                green %= num_pixels
                shiftG = False

        else:
            shiftG = True


        clrs[red] = (intensity, 0, 0)
        clrs[green] = (clrs[green][0], intensity, 0)
        clrs[blue] = (clrs[blue][0], clrs[blue][1], intensity)
        
    for i in range(num_pixels):
        np[i] = clrs[i]
    np.show()
