#import the module
import time
from turtle import *
color="blue"
#marker for drawing
pen = Turtle()
bgcolor("green")
fillcolor(color)
#Drawing an euilateral triangle
for i in range(6):
    begin_fill()
    fillcolor(color)
    pencolor("red")
    pen.forward(100) #move marker forward
    pen.left(60)    #tilt it to 120 degree
    end_fill()
pen.left(60)
pen.forward(100)
pen.left(60)
pen.forward(100)
pen.backward(100)
pen.right(120)
pen.forward(100)
time.sleep(20)