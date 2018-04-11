# Ziphalo Projects

These are programs that use the [ziphalo](https://www.kitronik.co.uk/5625-zip-halo-for-the-bbc-microbit.html) lights from [kitronik](https://www.kitronik.co.uk/).
This is a ring of 24 RGB LEDS which can be controlled using the
[neopixel](http://microbit-micropython.readthedocs.io/en/latest/neopixel.html) module of [micropython](http://microbit-micropython.readthedocs.io/en/latest/index.html).

* `bluehalo.py`  Sends a blue light around the ring.
* `circuit.py`  Sends two lights around the ring in opposite
   directions.  The lights gradually change hue.
* `ball.py`  The idea of this one is to create balls of different
   colour around the ring which then move under gravity and bounce off
   each other.  If two of the same colour collide, they annihilate.
* `gravity.py`  A single light moves under gravity (leaving a trail)
* `clock.py`  This is a bit like a stopwatch.  A red light travels
   round the ring (taking 1 second) and each time it passes the green
   light, it bumps it on one place.  Similarly, the blue light gets
   bumped by the green.  Press button A to start and stop.
* `down.py`  Uses the accelerometer to figure out which way is up.
* `chase.py` A simple chase game.  Use gravity to control the blue
  light, try to catch the green lights but avoid the red ones.

The other programs were used in experimenting.
