import turtle
import time
from turtle import *
pen=turtle.Turtle()
window=turtle.Turtle()
color=("violet","Indigo","blue","Green","yellow","orange","red")
pen.speed(20)
turtle.setup(425,425,100,500)   # width height startx starty
pen.width(3)
for i in range(4):
    for j in range(360):
        pen.color(color[i%7])
        pen.right(1)
        pen.forward(1)

    pen.right(90)
    pen.forward(50)
    
