import mbhandler
import pyautogui

width, height = pyautogui.size()

mbhandler.init()

SENSITIVITY = 5

try:
    while True:
        mb = mbhandler.queue.get()
        x = mb['accelerometer']['x']
        y = mb['accelerometer']['y']
        if abs(x) < SENSITIVITY:
            x = 0
        if abs(y) < SENSITIVITY:
            y = 0
        pyautogui.moveRel(x,-y)
        if mb['button_a']['down']:
            pyautogui.mouseDown()
        if mb['button_a']['up']:
            pyautogui.mouseUp()
        if mb['button_b']['down']:
            pyautogui.mouseDown(button='right')
        if mb['button_b']['up']:
            pyautogui.mouseUp(button='right')
except KeyboardInterrupt:
    pass

mbhandler.quit()
