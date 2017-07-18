#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter

# top = Tkinter.Tk()

# top.mainloop()


from Tkinter import *

root = Tk()

li = ['C','Python','php','sql','java']

movie = ['css','jquery','bootstrap']

hah = ['good','happy','shit']

listb = Listbox(root)

listb2 = Listbox(root)

listb3 = Listbox(root)

for item in li:
    listb.insert(0,item)

for item in movie:
    listb2.insert(0,item)

for item in hah:
    listb3.insert(0,item)

listb.pack()

listb2.pack()

listb3.pack()

root.mainloop()
