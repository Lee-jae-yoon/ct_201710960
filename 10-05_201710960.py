import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()

def drawTriangleAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    for i in range (0,3):
        t1.forward(size)
        t1.write(t1.pos())
        t1.left(120)

def drawPentagon(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    for i in range (0,5):
        t1.forward(size)
        t1.write(t1.pos())
        t1.left(72)

def drawStarAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    for i in range (0,5):
        t1.forward(size)
        t1.write(t1.pos())
        t1.right(144)

drawTriangleAt(-100,0,50)
drawPentagon(0,0,50)
drawStarAt(100,0,50)

wn.exitonclick()