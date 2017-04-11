import mbhandler
import getch
import threading
import queue

key = queue.Queue()
RUNNING = True

def keypress():
    global RUNNING
    while RUNNING:
        try:
            k = getch.getch()
            try:
                key.put(k)
            except key.Full:
                pass
        except KeyboardInterrupt:
            RUNNING = False
        except EOFError:
            RUNNING = False

keyThread = threading.Thread(target=keypress)
keyThread.daemon = True
keyThread.start()

mbhandler.init(output="raw")

listening = False

spin = ["|","/","-","\\"]
spinIndex = 0

print("Press <ENTER> to start")


try:
    while RUNNING:
        if not key.empty():
            k = key.get()
            if k == "\n":
                listening = True
        else:
            if listening:
                print("\rWaiting: " + spin[spinIndex], end='')
                spinIndex += 1
                spinIndex %= 4

        if not mbhandler.queue.empty():
            msg = mbhandler.queue.get()
            if listening:
                print("\n" + msg + " pressed first")
                print("Press <ENTER> to start")
                listening = False
except KeyboardInterrupt:
    pass
