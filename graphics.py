import turtle
turtle.speed(1)

t = turtle.Turtle()
turtle.bgcolor("black")
turtle.speed(0)

for i in range(50):

    for colors in ['red', 'magenta', 'blue', 'green', 'yellow', 'orange']:
        turtle.color(colors)
        turtle.pensize(3)
        turtle.left(12)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
