# Skier Game with PyGame

## Introduction

This is a simple [PyGame](http://www.pygame.org) program where you
control the motion of a skier by tilting a microbit, with the aim of
dodging the trees and collecting the gems.

## Installation

From this directory, only the file [`skier.py`](skier.py) is needed.
It runs using the [`mbhandler`](../mbhandler) module which needs to be
installed somewhere that `skier.py` can find it.  As well as the
modules needed for `mbhandler`, this program also uses:

* pygame
* sys
* random
* time
* math

The images for the skier, trees, and gems are all from
[OpenClipart](https://openclipart.org).  I used:

* [skier](https://openclipart.org/detail/76999/ski-silhoette)
* [fir tree](https://openclipart.org/detail/181473/douglas-fir)
* [gem](https://openclipart.org/detail/196319/crystal-gems-glittering-blue-yellow-precious-gems) (clipped to just one of them)

## Old Code

The file `mbevent.py` was used before I refactored the micro:bit handling code into its own module.
