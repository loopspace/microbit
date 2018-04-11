from microbit import *
import neopixel
import math

num_pixels = 24
np = neopixel.NeoPixel(pin0, num_pixels)
np.clear()

running = False
st = running_time()
et = running_time()
dt = "0"

stepTime = 1000/num_pixels

intensity = 127

red = 0
green = 0
blue = 0

shiftG = False
shiftB = False

while True:
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


    gx = accelerometer.get_x()
    gy = accelerometer.get_y()
    a = math.floor(math.atan2(gy,gx)/math.pi*12 - 5.5)%num_pixels
            
    for i in range(num_pixels):
        np[i] = (0,0,0)
    np[(red+a)%num_pixels] = (intensity, 0, 0)
    np[(green+a)%num_pixels] = (np[(green+a)%num_pixels][0], intensity, 0)
    np[(blue+a)%num_pixels] = (np[(blue+a)%num_pixels][0], np[(blue+a)%num_pixels][1], intensity)
        
    np.show()

    if button_a.was_pressed():
        if running:
            running = False
            dt = str((running_time() - st)/1000)
            display.show(dt)
        else:
            running = True
            display.clear()
            et = running_time()
            st = running_time()
            red = 0
            green = 0
            blue = 0
            shiftG = False
            shiftB = False

    if button_b.was_pressed() and not running:
        display.show(dt)
        
