import turtle
import mbhandler

mbhandler.init()

colours = [
    "Red",
    "Green",
    "Blue",
    "Yellow",
    "Purple",
    "Cyan"
]
colour = 0
turtle.pencolor(colours[colour])

while True:
    mb = mbhandler.queue.get()
    x = mb['accelerometer']['x']
    y = mb['accelerometer']['y']
    a = mb['button_a']['down']
    b = mb['button_b']['down']

    if abs(x) < 10:
        x = 0
    if abs(y) < 10:
        y = 0

    if abs(y) > abs(x):
        turtle.forward(-y)
    else:
        turtle.right(x)
        

    if b:
        colour += 1
        colour %= len(colours)
        turtle.pencolor(colours[colour])

    if a:
        if turtle.isdown():
            turtle.penup()
        else:
            turtle.pendown()


