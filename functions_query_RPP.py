#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyodbc import *
from tkinter import *
from tkinter import ttk
from query_RPP import *
from PIL import Image

def BD_conn_up():
    conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 11 for SQL Server};'
    r'SERVER=test;'
    r'DATABASE=test;'
    r'UID=user;'
    r'PWD=password'
    )

def BD_conn_down():
    cnxn.close()

# Data Entry
fields = 'Delegación', 'Año', 'Tomo', 'Acta', 'DNI', 'Nombre', 'Apellido'

def fetch(entries, r):
    rr = r
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        if (field == "Delegación"):
            var_del = text
        elif (field == "Año"):
            var_ano = text
        elif (field == "Tomo"):
            var_tomo = text
        elif (field == "Acta"):
            var_acta = text
        elif (field == "DNI"):
            var_dni = text
        elif (field == "Nombre"):
            var_nom = text
        elif (field == "Apellido"):
            var_ape = text
    #print('%s: "%s"' % (field, text))
    search(var_del, var_ano, var_tomo, var_acta, var_dni, var_nom, var_ape, rr)

def search(deleg, ano, tomo, acta, dni, nom, apell, root):
    cursor = cnxn.cursor()
    cursor.execute(#####Consulta#####)
    rows = cursor.fetchone()
    c = 1
    for row in rows:
        archivo=row[12]
        Lb = Label( root, textvariable = row, relief = RAISED, bd=0, pady="3" )
        Lb.pack()
        root.bind('<Return>', (lambda event, f=archivo: open_file(f)))
        B = Button(root, text='Ver', command=(lambda f=archivo: open_file(f)))
        B.pack(anchor="e")
        c = c + 1
    cnxn.close()




def show_results(root):
    flag = 'OK'
    if (flag == 'OK'):
        archivo = (r"C:\Users\Juan Ignacio\Pictures\2.jpg")
        #T = Text(root)
        #T.pack(side=RIGHT, padx=5, pady=5)
        #T.insert(END, 'acta tal')
        root.bind('<Return>', (lambda event, f=archivo: open_file(f)))
        B = Button(root, text='Ver', command=(lambda f=archivo: open_file(f)))
        B.pack()
        Lb = Listbox(root)
        Lb.insert(1,"Python")
        Lb.pack()
    else:
        T = Text(root)
        T.pack(side=RIGHT, padx=5, pady=5)
        T.insert(END, "No se encontraron resultados")


    #root.mainloop()

def open_file(path):
    imagen = Image.open(path)
    imagen.show()

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries
