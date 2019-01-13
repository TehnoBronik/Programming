import math
from random import *
from tkinter import *
def mycircule(x_cntr, y_cntr, r, color):
    canvas.create_oval(x_cntr, y_cntr, x_cntr+r, y_cntr+r, fill=color)
def mytriangule (x_cntr, y_cntr, r, fill=color):
    xb=x_cntr
    yb=y_cntr+r
    g=r*r
    h=(r/2)*(r/2)
    am=math.sqrt(g-h)
    xa=x_cntr-am
    ya=y_cntr-(r/2)
    xc=x_cntr+am
    yc=y_cntr-(r/2)
    canvas.create_line(xa,ya,xb,yb)
    canvas.create_line(xb,yb,xc,yc)
    canvas.create_line(xc,yc,xa,ya)
root = Tk()
canvas = Canvas(root, width=600, height=600)
canvas.pack()
diapason = 0
while True:
    colors = choicecolors = choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange',
                  'pink', 'purple', 'red','yellow', 'violet', 'indigo', 'chartreuse', 'lime'])
    x0 = randint(0, 600)
    y0 = randint(0, 600)
    d = randint(0, 600/5)
    mycircule(x0, y0, d, colors)
    mytriangule(x0, y0, d, colors)
    root.update()
