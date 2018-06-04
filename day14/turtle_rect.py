import turtle

color= ("violet","Indigo","blue","Green","yellow","orange","red")
j=0
class MyException(Exception):pass
def draw_sq(x):
    global j
    pen.color(color[j])
    pen.width(4)
    for i in range (2):
        pen.forward(x)
        pen.right(90)
    j =(j+1)%7
    draw_small(x)
    
def draw_small(x):
    try:
       if x > 0:
           x = x-10
           draw_sq(x)
       else:
            raise Myexception()
    except:
        print 'done successfully'
        turtle.bye()
    

pen = turtle.Turtle()
x = input("enter size of rect")
draw_sq(x)
