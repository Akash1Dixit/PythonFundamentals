from Tkinter import *
import random
    
root = Tk()
     
languages = ['Python','Perl','C++','Java','Tcl/Tk']
for i in range(5):
   l = Label(root, 
                text=languages[i], 
                fg='Black', 
                bg='white')
   l.place(x = 20, y = 30 + i*30, width=150, height=25)
          
mainloop()
