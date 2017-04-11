# Test Your Reactions

This is a simple reaction test project.  The idea is to program a
micro:bit to send a string (a _name_) via the radio upon a trigger.
The included script does so when button A is pressed, but one could
use other triggers such as shaking or tilting the micro:bit.

There are three programs which can be run on a computer to listen for
these names.  These can be used to set up a competition between teams.

## The Programs

* ['speed_pygame.py'](speed_pygame.py) This uses
  ['pygame'](http://www.pygame.org) and is the most advanced of the
  programs.  Click to start a round, then when the screen turns green
  it is the first to send a signal that wins the round.  Sending a
  signal before the screen turns green disqualifies that micro:bit
  from that round.
* ['speed_tk.py'](speed_tk.py) This uses
  ['tkinter'](https://wiki.python.org/moin/TkInter).  It's not as
  sophisticated as the pygame version, but runs along the same lines.
* ['speed_pc.py'](speed_pc.py) This is a command line version.

