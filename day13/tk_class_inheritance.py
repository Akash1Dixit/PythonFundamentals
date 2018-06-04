from Tkinter import *
from tk_class import Hello

parent = Frame(None)
parent.pack()
Hello(parent).pack(side=LEFT)

Button(parent,text='click me',command = exit , fg = 'white' ,bg='black').pack(side=RIGHT)
parent.mainloop()
