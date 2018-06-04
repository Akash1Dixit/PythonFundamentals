from Tkinter import *
root = Tk()

# family,size and style
#labelfont = ('times',40,'bold')
label = Label(root, text = 'Python is fun')

#green text on black label
label.config(fg='green',bg='black')

#use a larger font
#label.config(font = labelfont)
label.config(font=('times',40,'bold'))

#shape of cursor other are: cross,pirate,hand2,watch
label.config(cursor = 'watch') 

#initial size:lines,chars , border width and style
label.config(height = 3, width = 20,bd=8,relief = GROOVE)

#adds empty space around the widget
label.pack(padx=20,pady=20,expand = YES,fill =BOTH)
root.mainloop()
