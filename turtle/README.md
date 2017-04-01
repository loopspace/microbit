# Turtle Scripts

## Introduction

These scripts are some experiments with a view to using the microbit to control the turtle in Python's turtle module.

The scripts were written at various stages of how I handled communication between the micro:bits and the PC.  I keep them all to chart the progress, but they divide into those that use the [`mbhandler`](../mbhandler) module and those that predate it.

## Current Scripts

* [`mbturtle.py`](mbturtle.py) Simple drawing program.  Tilt control for the turtle.  Button B cycles through colours.  Button A toggles pen up/down.
* [`mbturtledriver.py`](mbturtledriver.py) A little more sophisticated control, with the tilt now affecting the *acceleration* of the turtle.
* [`twoturtles.py`](twoturtles.py) Uses two portable micro:bits to control two separate turtles on the same canvas.  The portable micro:bits need to have distinct names set in their respective programs ([`mb_radio_sender.py`](../mbhandler/mb_radio_sender.py)).


## Old Scripts

* [`turtleclient.py`](turtleclient.py) Similar to `mbturtle.py` except predates the existence of the `mbhandler` module.
