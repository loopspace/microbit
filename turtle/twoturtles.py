import turtle
import mbhandler

mbhandler.init()
width,height = turtle.screensize()

colours = [
    "Red",
    "Green",
    "Blue",
    "Yellow",
    "Purple",
    "Cyan"
]

turtles = {}
turtles["Niphredil"] = {
    'turtle': turtle.Turtle(),
    'speed': 0,
    'colour': 0
}
turtles["Alfirin"] = {
    'turtle': turtle.Turtle(),
    'speed': 0,
    'colour': 0
}

turtles["Niphredil"]['turtle'].pencolor(colours[turtles["Niphredil"]['colour']])
turtles["Alfirin"]['turtle'].pencolor(colours[turtles["Alfirin"]['colour']])

while True:
    mb = mbhandler.queue.get()
    name = mb['name']
    x = mb['accelerometer']['x']
    y = mb['accelerometer']['y']
    a = mb['button_a']['down']
    b = mb['button_b']['down']

    if abs(x) < 10:
        x = 0
    if abs(y) < 10:
        y = 0

    if abs(y) > abs(x):
        turtles[name]['speed'] -= y/100
    else:
        turtles[name]['turtle'].right(x)

    for t in turtles:
        turtles[t]['turtle'].forward(turtles[t]['speed'])
        tx,ty = turtles[t]['turtle'].position()
        if tx < -width:
            angle = turtles[t]['turtle'].heading()
            if angle > 90 and angle < 270:
                turtles[t]['turtle'].setheading(180 - angle)
                turtles[t]['turtle'].setposition(-2*width - tx,ty)
        elif tx > width:
            angle = turtles[t]['turtle'].heading()
            if angle < 90 or angle > 270:
                turtles[t]['turtle'].setheading(180 - angle)
                turtles[t]['turtle'].setposition(2*width - tx,ty)
        if ty < -height:
            angle = turtles[t]['turtle'].heading()
            if angle > 180:
                turtles[t]['turtle'].setheading(- angle)
                turtles[t]['turtle'].setposition(tx,-2*height - ty)
        elif ty > height:
            angle = turtles[t]['turtle'].heading()
            if angle < 180:
                turtles[t]['turtle'].setheading( - angle)
                turtles[t]['turtle'].setposition(tx,2*height - ty)
        

    if b:
        turtles[name]['colour'] += 1
        turtles[name]['colour'] %= len(colours)
        turtles[name]['turtle'].pencolor(colours[turtles[name]['colour']])

    if a:
        if turtles[name]['turtle'].isdown():
            turtles[name]['turtle'].penup()
        else:
            turtles[name]['turtle'].pendown()


