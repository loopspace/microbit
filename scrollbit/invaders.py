from microbit import *
import random
import scrollbit

char = Image("00000:"
             "00000:"
             "00000:"
             "00900:"
             "09990:")

ts = 0
cs = 5
bullets = []
bombs   = []
score   = 0
state   = 0

while True:
    if state == 0:

        scrollbit.clear()
        scrollbit.set_pixel(ts,0,50)
        scrollbit.draw_icon(cs,2, char, brightness = 50)
        for b in bullets:
            scrollbit.set_pixel(b[0],b[1],50)
            if b[1] == 0 and b[0] == ts:
                display.set_pixel(score%5, score//5, 5)
                score += 1
                if score == 25:
                    score = 0
                    ts = 0
        
            b[1] -= 1

        for b in bombs:
            scrollbit.set_pixel(b[0],b[1],50)
            if b[1] == 6 and abs(b[0] - cs - 2) < 2:
                score -= 1
                if score < 0:
                    scrollbit.clear()
                    scrollbit.show()
                    scrollbit.scroll("Game Over", brightness = 50)
                    display.show(Image.ARROW_E)
                    state = 1
                else:
                    display.set_pixel(score%5, score//5, 0)
                cs = 0
        

            b[1] += 1
            b[0] += 1

        bullets[:] = [b for b in bullets if b[1] >= 0]
        bombs[:]   = [b for b in bombs if b[1] < 7 and b[0] < 17]

        scrollbit.show()

        ts += 1
        if ts > 16:
            ts = 0
        if accelerometer.get_x() < -127:
            cs += 1
        elif accelerometer.get_x() > 127:
            cs -= 1
        if cs > 13:
            cs = 13
        if cs < -1:
            cs = -1
        if button_a.was_pressed():
            bullets.append([cs+2,4])

        if random.random() > 0.9:
            bombs.append([ts,0])
        sleep(50)
    else:
        scrollbit.clear()
        if button_b.was_pressed():
            display.clear()
            ts = 0
            cs = 5
            bullets = []
            bombs   = []
            score   = 0
            state   = 0


