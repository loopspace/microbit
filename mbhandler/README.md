# MBHandler

## Introduction

This directory contains the core files for the `mbhandler` module
which handles the communication between a separate microbit and
another device, using a second microbit as a relay.

## Files


* [`mb_radio_sender.py`](mb_radio_sender.py) should be flashed to the
  handheld microbit.
* [`mb_radio_receiver.py`](mb_radio_receiver.py) should be flashed to
  the receiver microbit.
* [`mbhandler.py`](mbhandler.py) is a utility python module that can
  be run on a suitable device to interpret the readings from the
  microbits.  It looks for the receiver microbit connected to a USB
  port and then listens for messages from it.  It does some processing
  on the messages to make them easier to interpret by the main
  program.
* [`mbhandler_test.py`](mbhandler_test.py) is a test script to ensure
  that everything is working.

## Instructions

You need two microbits to use this module.  One is the sender and the
other the receiver.  The sender is handheld and should be battery
powered to allow fully movement.  The receiver is connected to
whatever device is to be controlled via a USB cable.

1. Flash the two scripts onto the microbits.
2. Put the file `mbhandler.py` somewhere that your Python scripts can
find it.

To test the system, run `mbhandler_test.py`.  This simply reads the
data off the portable microbit and displays it on the console.

It is also a good example of how to use the `mbhandler` module.

~~~
# Import the module
import mbhandler

# Initialise the module
mbhandler.init()

while True:
    # Read a message from the queue
	print(mbhandler.queue.get())
~~~

There is also a method `mbhandler.quit()` which should be called when
the script exits.  It's probably not *bad* if it doesn't get called
but does ensure that the various bits of the `mbhandler` module close
down nicely rather than abruptly.

## Configuration

The `mbhandler.init()` can take key-value pairs specifying options.
At present, there is only one option available:

* `method`: if this is set to `pygame` then the module uses PyGame's
  event handling to pass the information from the microbit.

Later versions of the module may provide more options.
