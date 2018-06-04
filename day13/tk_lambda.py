from Tkinter import *

def handler(a,b):
    print a,b

def func():
    x=43
    Button(text='click',command = (lambda:handler(x,'spam'))).pack()

func()
mainloop()
