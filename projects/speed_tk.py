import tkinter
import tkinter.font
import mbhandler

spin = ["|","/","-","\\"]
spinIndex = 0

mbhandler.init(output="raw")

root = tkinter.Tk()
root.title("Quiz")
frame = tkinter.Frame(root,width="200px",height="200px")
frame.grid_propagate(0)
frame.pack()

font = tkinter.font.Font(family='TeX Gyre Pagella', size=20)

b = tkinter.Button(frame, text="Click to start", font=font)
q = tkinter.Button(frame, text="Quit", font=font)

w = tkinter.Label(frame, justify=tkinter.RIGHT, text="Waiting ",font = font)
spinVar = tkinter.StringVar()
sp = tkinter.Label(frame, justify=tkinter.LEFT, textvariable=spinVar, font=font)
w.grid(sticky=tkinter.E,row=0)
sp.grid(sticky=tkinter.W,row=0,column=1)

m = tkinter.Label(frame, justify=tkinter.RIGHT, text="Team ",font = font)
mbVar = tkinter.StringVar()
mb = tkinter.Label(frame, justify=tkinter.LEFT, textvariable=mbVar,font = font)
m.grid(sticky=tkinter.E,row=0)
mb.grid(sticky=tkinter.W,row=0,column=1)

b.grid(sticky=tkinter.W,row=2)
q.grid(sticky=tkinter.SE,row=3)
w.grid_remove()
sp.grid_remove()
m.grid_remove()
mb.grid_remove()

def start():
    while not mbhandler.queue.empty():
        mbhandler.queue.get()
    b.grid_remove()
    m.grid_remove()
    mb.grid_remove()
    w.grid()
    sp.grid()
    root.after(100,update)

def update():
    if not mbhandler.queue.empty():
        msg = mbhandler.queue.get()
        mbVar.set(msg)
        b.config(text="Click to restart")
        w.grid_remove()
        sp.grid_remove()
        b.grid()
        m.grid()
        mb.grid()
        root.update()
    else:
        global spinIndex
        spinIndex += 1
        spinIndex %= 4
        spinVar.set(spin[spinIndex])
        root.update()
        root.after(100,update)

def finish():
    root.destroy()
    
b.config(command=start)
q.config(command=finish)

root.mainloop()
