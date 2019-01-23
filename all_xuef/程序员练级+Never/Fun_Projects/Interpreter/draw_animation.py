import turtle

screen = turtle.Screen()    # create a new screen
screen.setup(500,500)       # 500 x 500 window

don = turtle.Turtle()       # create a new [ninja] turtle
don.speed(0)                # make it move faster

def draw_square() :         # a function that draws one square
    for side in range(4) :
        don.forward(100)
        don.left(90)

don.penup()                 # go off-screen on the left
don.goto(-350, 0)
don.pendown()

while True :                # now do this repeatedly, to animate :
    don.clear()             # - clear all the turtle's previous drawings
    draw_square()           # - draw a square
    don.forward(10)         # - move forward a bit
