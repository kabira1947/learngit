import turtle
t=turtle.Turtle()
t.color("cyan")
t.speed(0)

colors=['green','blue','yellow','red','orange','purple','cyan','green','blue','yellow','red','orange','purple','cyan']

def square(color):
    for side in range(4):
        t.forward(100)
        t.right(90)
        for side in range(4):
            t.forward(50)
            t.right(90)
t.penup()
t.back(40)
t.pendown()

for color in colors:
    t.color(color)
    square(colors)
    t.forward(50)
    t.left(45)
t.hideturtle()