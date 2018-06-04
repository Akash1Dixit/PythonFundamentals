from Tkinter import *

class Hello(Frame):
    def __init__(self,parent = None):
        Frame.__init__(self,parent)
        self.pack()
        self.data = 0
        self.widgets()

    def widgets(self):
        button=Button(self,text="click!",command= self.message , fg='black',bg='lightblue')
        button.pack(side=LEFT)

    def message(self):
        self.data+=1
        print 'program running %s time' %self.data

if __name__ == '__main__':
    print 'In tk_class'
    Hello().mainloop()
