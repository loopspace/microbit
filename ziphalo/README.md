# Ziphalo Projects

These are programs that use the [ziphalo]() lights from [kitronik]().
This is a ring of 24 RGB LEDS which can be controlled using the
[neopixel]() module of [micropython]().

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
