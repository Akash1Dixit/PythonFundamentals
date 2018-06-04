from Tkinter import *

master = Tk()

w = Scale(master, from_=100, to=0, orient=VERTICAL)
w.pack()
print w.get()
w = Scale(master, from_=0, to=100, orient=HORIZONTAL)
w.pack()
print w.get()
mainloop()
