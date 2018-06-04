#import the module
from turtle import *
import time

wn = Screen()

#adding background color
wn.bgcolor("black")

#setting background image
#wn.setup(500,500)
#wn.bgpic("im1.gif")

#setting title
wn.title("Drawing Triangle")

#marker for drawing
pen = Turtle()

#changing pen color
pen.color("green")

#changing pen width
pen.width(2)

#setting pen speed
pen.speed(2)

#some other methods 
pen.up()
pen.goto(50,50)
pen.down()

#Drawing an euilateral triangle
for i in range(3):
    pen.forward(100) #move marker forward
    pen.left(120)    #tilt it to 120 degree
time.sleep(2)

#shut the turtle graphics screen
#bye()
