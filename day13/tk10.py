from Tkinter import *

def onButtonPress():
    labelVariable.set('welcome')

#main window
root = Tk()

#GUIs
#label and button
labelVariable = StringVar() #string variable
#textvariable associates a Tkinter variable (usually a StringVar) with the label.
#If the variable is changed, the label text is updated. 
label =Label(root,textvariable=labelVariable,
                              anchor="center",fg="green",bg="black")
#initialize the variable
labelVariable.set("Hello !")
label.grid(column=0,row=0)

button = Button(root,text = 'click' ,command = onButtonPress)
button.grid(column=1,row=0)

root.mainloop()
