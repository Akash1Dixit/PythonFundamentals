#
#import the module Tkinter


from Tkinter import *
root.mainloop( )

#Create the GUI application main window
root = Tk( )
root.title("A simple application")

#Add one or more widgets to the GUI application.
label=Label(root,text='hello world!!')

#pack the Label in the parent widget
label.pack()

#Adding a button and packing it in the same statement
Button(text='click', command= exit).pack()

#calls the mainloop to bring up the window and start the tkinter event loop
