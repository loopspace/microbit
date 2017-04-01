# BBC Microbit Examples

## Introduction

This is my testing ground for the BBC Microbit.
I'm using micropython, via the [mu](https://github.com/ntoll/mu)
editor.

## Projects

### Remote control via microbit

These projects involve using two microbits to control something.  One
microbit is handheld and sends a radio message to the other with
readings from its sensors.  The second microbit can then be connected
to a device which can use those readings.


#### [mbhandler](mbhandler/)

This provides the handler module which deals with the communication
between the microbits and whatever device is being used to deal with
that information.

#### [ski](ski/)

This is a simple game using [`pygame`](http://www.pygame.org/).  Avoid
the trees and collect the gems.  The microbit controls the player's
left and right movement.

#### [turtle](turtle/)

This is a variety of scripts that use the microbit to draw using the
`turtle` module.

#### [lego](lego/)

These are some projects that involve controlling a lego robot with a
microbit connected to it.  The EV3 robots work using
['ev3dev'](http://www.ev3dev.org/) on the brick and a python script
using [`mbhandler`](mbhandler).  The RCX2.0 robot is a bit more
complicated as the receiving microbit has to be hooked up to a sensor.
