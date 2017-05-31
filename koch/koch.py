import turtle

# draw Koch fractal and Koch snowflakes
def koch(t, order, size):
    # base case
    if order == 0:
        t.forward(size)
        
    # start recursion
    else:
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)
        
# koch function with simpler code
def koch_simpler(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            kock_simpler(t, order-1, size/3)
            t.left(angle)

# create a Turtle object called k
k = turtle.Turtle()

# specify speed, color, shape of object k
k.speed(3)
k.color("black")
k.shape("turtle")

# create a background
background = turtle.Screen()
background.bgcolor("white")
background.exitonclick()

# draw a koch fractal with an order of 3
koch(k, 3, 180)

# draw Koch snowflakes
for i in range(3):
    koch(k, 2, 270)
    k.right(120)
