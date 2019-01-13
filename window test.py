import matplotlib.pyplot as plt
from random import *
from tkinter import *
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
    mytriangule(x0, y0, d, colors )
    root.update()
def mycircule(x_cntr, y_cntr, r, color)
    canvas.create_oval(x_cntr, y_cntr, x_cntr+r, y_cntr+r, fill=color )
def mytriangule (x_cntr, y_cntr, r, color)
    plt.plot([-1.0, 1.0], [0.0, 1.0])
