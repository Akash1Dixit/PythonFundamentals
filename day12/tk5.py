from Tkinter import *
#import tkMessageBox
#import Tkinter

top = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()

#The control VARIABLE tracks the current state of the checkbutton.
#Normally this variable is an IntVar, and 0 means cleared and 1 means set,
#but you can change these values using the onvalue and offvalue options.

C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0)
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0)
C1.pack()
C2.pack()
top.mainloop()
