from random import *
from tkinter import *
root = Tk()
canvas = Canvas(root, width=1600, height=1200)
canvas.pack()
diapason = 0
while True:
    colors = choicecolors = choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange',
                  'pink', 'purple', 'red','yellow', 'violet', 'indigo', 'chartreuse', 'lime'])
    x0 = randint(0, 1920)
    y0 = randint(0, 1080)
    d = randint(0, 1080/5)
    canvas.create_oval(x0, y0, x0+d, y0+d, fill=colors )
    root.update()
