# !/usr/bin/python3
from tkinter import *
import tkinter as tk
from PIL import Image



root = Tk()
var = IntVar()
archivo = (r"C:\Users\Juan Ignacio\Pictures\2.jpg")
row = StringVar()
for i in range(1,10):
    row.set(" Hey!? How are you doing? Hey!? How are you doing? Hey!? How are you doing? Hey!? How are you doing?")
    Lb = Label( root, textvariable = row, relief = RAISED, bd=0, pady="3" )
    Lb.pack()
    root.bind('<Return>', (lambda event, f=archivo: open_file(f)))
    B = Button(root, text='Ver', command=(lambda f=archivo: open_file(f)))
    B.pack(anchor="e")

def open_file(path):
    imagen = Image.open(path)
    imagen.show()




#label = Label(root)
#label.pack()
root.mainloop()
