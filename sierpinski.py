import turtle

# show two ways to draw Sierpinski triangle

# First way draw Sierpinski triangle
def sierpinski_tri(t, order, size):
    # base case
    if order == 0:
        t.forward(size)
        t.left(120)
        t.forward(size)
        t.left(120)
        t.forward(size)
        t.left(120)
    else:
        sierpinski_tri(t, order-1, size/2)
        t.forward(size/2)
        sierpinski_tri(t, order-1, size/2)
        t.left(120)
        t.forward(size/2)
        t.right(120)
        sierpinski_tri(t, order-1, size/2)
        t.right(120)
        t.forward(size/2)
        t.left(120)
        
        

# create a turtle object called s
s = turtle.Turtle()
s.color("black")
s.shape("turtle")
s.speed(2)

# create a background
window = turtle.Screen()
window.bgcolor("white")

sierpinski_tri(s, 4, 120)

#################################
# Second way to draw a Sierpinski triangle
# Credits: This code was written by editing the code from http://www.lpb-riannetrujillo.com/blog/python-fractal/

myPen = turtle.Turtle()
myPen.ht()
myPen.speed(5)
myPen.pencolor('orange')

points = [[-175,-125],[0,175],[175,-125]] #size of triangle

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2) #find midpoint

def triangle(points,depth):

    myPen.up()
    myPen.goto(points[0][0],points[0][1])
    myPen.down()
    myPen.goto(points[1][0],points[1][1])
    myPen.goto(points[2][0],points[2][1])
    myPen.goto(points[0][0],points[0][1])

    if depth>0:
        triangle([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   depth-1)
        triangle([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   depth-1)
        triangle([points[2],
                         getMid(points[2], points[1]),
                         getMid(points[0], points[2])],
                   depth-1)

triangle(points,4)
