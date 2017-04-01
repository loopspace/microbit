# Microbit+Lego

## Introduction

The programs in this directory are for using a microbit to control
with a Lego Mindstorms robot.  This is easiest for a robot built with
the [ev3](https://www.lego.com/en-gb/mindstorms) brick as it is
possible to put a Linux distribution on that via
[ev3dev](http://www.ev3dev.org/) and plug the microbit directly into
the brick via a USB cable.  Then one can write programs in whatever
language one likes.  I've also experimented with an older Mindstorms
RCX2.0 brick.  This is a little more complicated.

## EV3

These programs all use the [`mbhandler`](../mbhandler) module.  The
receiver microbit is plugged in to the EV3 block via the USB port.
The `mbhandler` module depends on the following Python modules:

* serial
* threading
* warnings
* queue

These may all be installed as standard on ev3dev; if not, you will
need to install them.  Also, the `mbhandler.py` file should be
installed somewhere that the script can find it.

All the following scripts provide essentially the same functionality:
driving and steering via tilt control and extra features via button
press (if available).
If made executable, they can be run from the Brickman interface.

These are somewhat experimental, in particular that at times I've used
"magic numbers" rather than programmatically determining the right
ones to use.  For example, in R3ptar then pressing a button makes the
snake's head strike and this involves moving a motor to a particlar
position.

* `edubot.py` This is for the base robot made with the Education kit.
* `Gripp3r.py` This is for the
  [Gripp3r](https://www.lego.com/en-gb/mindstorms/build-a-robot/gripp3r)
  robot with the Home kit.  This doesn't actually use the `mbhandler`
  module as it was written prior to that being separated into its own
  code, so it needs updating.
* `R3ptar.py` This is for the
  [R3ptar](https://www.lego.com/en-gb/mindstorms/build-a-robot/r3ptar)
  robot.  It only needs one piece changing to ensure that the USB port
  is clear.
* `Track3r.py` This is for the
  [Track3r](https://www.lego.com/en-gb/mindstorms/build-a-robot/track3r)
  robot.  Note that this robot needs modification to expose the USB
  port.  Essentially, the command brick needs to be mounted higher so
  that it isn't blocked by the motors (this has a knock-on effect for
  the other parts, but the modifications are fairly straight-forward).

## RCX2.0

Programming the RCX2.0 is a little more complicated.  My solution has
been to turn the receiving microbit into a sensor.  This involves
cutting one of the RCX2.0 connection wires to expose the ends and
connecting them to the microbit pins.  Setting the voltage on the pin
allows the microbit to communicate with the RCX2.0.

This means that the programming is a little more intricate.
Effectively, the logic is divided between the receiving microbit and
the RCX brick.

The RCX scripts are written using [NQC](https://github.com/jverne/nqc.git).

* [`acrobot`](acrobot) These scripts are for the acrobot.
