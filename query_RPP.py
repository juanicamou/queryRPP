#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functions_query_RPP import *


if __name__ == '__main__':
    root = Tk()
    root.geometry('1200x500')
    root.configure(bg = 'white')
    root.title('Aplicación')
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e, root)))
    b1 = Button(root, text='Show',
          command=(lambda e=ents: fetch(e, root)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Quit', command=root.quit)
    b2.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()
