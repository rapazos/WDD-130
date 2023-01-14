from tkinter import *

root = Tk()
my_Canvas = Canvas(root, width=300, height=200, bg='white')
my_Canvas.pack()
my_Canvas.create_line(0,100,300,100,fill='red')


root.mainloop()