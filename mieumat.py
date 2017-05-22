import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()

def giyukat(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.fd(size)
    t1.right(90)
    t1.fd(size)
    
def nieunat(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.fd(size)
    t1.left(90)
    t1.fd(size)

def mieumat(x,y,size):
    giyukat(x,y,size)
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.setheading(270)
    nieunat(x,y,size)

mieumat(100,100,100)

wn.exitonclick()