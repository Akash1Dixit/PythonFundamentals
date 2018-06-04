from turtle import *

color= ["violet","Indigo","blue","Green","yellow","orange","red"]
color1= ["Green","yellow","orange","red","blue","Indigo","light blue"]
speed(10)
bgcolor("black")
for i in range(12):
    begin_fill()
    fillcolor(color1[i%7])
    width(4)
    pencolor(color[i%7])
    circle(60)
    right(10)
    end_fill()

bye()
