  from tkinter import *
    root = Tk()
    my_Canvas = Canvas(root, width=800, height=500, bg='white')
my_Canvas.pack()
my_Canvas.create_line(0,200,800,200,fill='green')
