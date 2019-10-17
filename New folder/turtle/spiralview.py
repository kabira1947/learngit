import turtle

t=turtle.Turtle()
t.color("cyan")
t.speed(0)
def spiral(lenght):
    for side in range(4):
        t.forward(lenght)
        t.right(90)
        for side in range(4):
            t.forward(50)
            t.right(90)
t.penup()
t.back(20)
t.pendown()

for square in range(80):
    spiral(5)
    t.forward(5)
    t.left(5)
t.hideturtle()
