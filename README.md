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


#### [mbhander](mbhandler/README.md)

This provides the utility programs.

* `mb_radio_sender.py` should be flashed to the handheld microbit.
* `mb_radio_receiver.py` should be flashed to the receiver microbit.
* `mbhandler.py` is a utility python module that can be run on a
  suitable device to interpret the readings from the microbits.  It
  looks for the receiver microbit connected to a USB port and then
  listens for messages from it.  It does some processing on the
  messages to make them easier to interpret by the main program.

#### ski

This is a simple game using [`pygame`](http://www.pygame.org/).  Avoid
the trees and collect the gems.  The microbit controls the player's
left and right movement.

#### turtle

This is a variety of scripts that use the microbit to draw using the
`turtle` module.

#### lego

These are some projects that involve controlling a lego robot with a
microbit connected to it.  The EV3 robots work using
['ev3dev'](http://www.ev3dev.org/) on the brick and a python script
using `mbhandler`.  The RCX2.0 robot is a bit more complicated as the
receiving microbit has to be hooked up to a sensor.

* `edubot.py` This is for the base robot made with the Education kit.
* `ev3dev_client.py` This is for the Grabb3r robot with the Home kit.
* `acrobot` These scripts are for the acrobot which is an RCX2.0
  robot.  The receiving microbit is hooked up to one of the sensor
  ports.  The script on the RCX2.0 is written in
  [NQC](https://github.com/jverne/nqc.git).
