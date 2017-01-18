import mbhandler

mbhandler.init()

while True:
    print(mbhandler.queue.get())
