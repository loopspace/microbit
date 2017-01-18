import turtle
import mbhandler

width,height = turtle.screensize()

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
speed = 0

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
        speed -= y/100
    else:
        turtle.right(x)
    turtle.forward(speed)

    tx,ty = turtle.position()
    if tx < -width:
        angle = turtle.heading()
        if angle > 90 and angle < 270:
            turtle.setheading(180 - angle)
            turtle.setposition(-2*width - tx,ty)
    elif tx > width:
        angle = turtle.heading()
        if angle < 90 or angle > 270:
            turtle.setheading(180 - angle)
            turtle.setposition(2*width - tx,ty)
    if ty < -height:
        angle = turtle.heading()
        if angle > 180:
            turtle.setheading(- angle)
            turtle.setposition(tx,-2*height - ty)
    elif ty > height:
        angle = turtle.heading()
        if angle < 180:
            turtle.setheading( - angle)
            turtle.setposition(tx,2*height - ty)

    if b:
        colour += 1
        colour %= len(colours)
        turtle.pencolor(colours[colour])

    if a:
        if turtle.isdown():
            turtle.penup()
        else:
            turtle.pendown()


