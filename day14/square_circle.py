import turtle
import time
from turtle import *
pen = turtle.Turtle()
window = turtle.Turtle()
color= ("violet","Indigo","blue","Green","yellow","orange","red")
pen.speed(5)
turtle.setup(425,425,100,500)
#turtle.goto(50,50)
pen.width(3)
for i in range(35):
    for j in range(4):
        pen.color(color[i%7])
        pen.forward(100)
        pen.right(90)
    pen.right(10)        
turtle.title("`Turtle Is Drawing")
turtle.write("Cool Isn't it", font=("Arial",20))
time.sleep(5)
turtle.bye()

