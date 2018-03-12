# !/usr/bin/python3
from tkinter import *
import tkinter as tk
from PIL import Image



root = Tk()
var = IntVar()
archivo = (r"C:\Users\Juan Ignacio\Pictures\2.jpg")
for i in range(1,10):
    Lb = Listbox(root)
    Lb.insert(i, "acta" + str(i))
    Lb.pack()
    root.bind('<Return>', (lambda event, f=archivo: open_file(f)))
    B = Button(root, text='Ver', command=(lambda f=archivo: open_file(f)))
    B.pack()

def open_file(path):
    imagen = Image.open(path)
    imagen.show()



#label = Label(root)
#label.pack()
root.mainloop()
