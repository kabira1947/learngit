import turtle


def spiral(sides,turn,color,width):
    t=turtle.Turtle()
    t.color(color)
    t.width(width)
    t.speed(0)
    for n in range(sides):
        t.forward(90)
        t.right(turn)
        t.penup()
        t.left(60)
        t.pendown()
        t.hideturtle()
spiral(700,600,'blue',5)

turtle.mainloop()