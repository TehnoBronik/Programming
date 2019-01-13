import math
from random import *
from tkinter import *
import time
def mycircule(x_cntr, y_cntr, r, color):
    canvas.create_oval(x_cntr, y_cntr, x_cntr+r, y_cntr+r, outline="white", fill=color)
def mytriangule (x_cntr, y_cntr, r):
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
root.wm_state('zoomed')
canvas = Canvas(root, width=600, height=600)
canvas.pack()
canvas.configure(background="black")

speed = [1, 1]
d = 200
x = 300
y = 200
img = PhotoImage(file='wondows.gif')
while True:
    canvas.delete("all")
    x += speed[0]
    y += speed[1]
    canvas.create_image(x, y, image = img, anchor = NW)
    root.update()
    time.sleep(0.01)
    if x<0 or x>600-259:
        speed[0]=-speed[0]
    if y<0 or y>600-186:
        speed[1]=-speed[1]
