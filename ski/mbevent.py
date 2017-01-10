import serial
import threading
import pygame

# Can we increment USEREVENT to avoid clashes?
MICROBITEVENT = pygame.USEREVENT
pygame.USEREVENT += 1
# These should be customisable via init
PORT = "/dev/tty.usbmodemFA132"
BAUD = 115200

def worker():
    s = serial.Serial(PORT)
    s.baudrate = BAUD
    s.parity = serial.PARITY_NONE
    s.databits = serial.EIGHTBITS
    s.stopbits = serial.STOPBITS_ONE
    
    while True:
        try: 
            data = s.readline().decode("ascii").rstrip()
        except:
            continue
        if data == 'None':
            continue
        data_s = data.split(":")
        if len(data_s) != 5:
            continue
        x = int(data_s[0])
        y = int(data_s[1])
        z = int(data_s[2])
        a = data_s[3] == 'True'
        b = data_s[4] == 'True'
        e = pygame.event.Event(MICROBITEVENT,x=x,y=y,z=z,a=a,b=b)
        pygame.event.post(e)


def init():        
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

# Should we clean up after ourselves?
