from tkinter import *
from tkinter import ttk

def savePosn(event):
    # se muestra la coordenada del clic izquierdo
    global lastx, lasty
    lastx, lasty = event.x, event.y
    print("Clic Izq:",event.x, event.y)

def addLine(event):
    canvas.create_line((lastx, lasty, event.x, event.y))
    # savePosn(event)
    print("???:",event.x, event.y)

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", savePosn)
canvas.bind("<B1-Motion>", addLine)

root.mainloop()