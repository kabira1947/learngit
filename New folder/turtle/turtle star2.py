import turtle

t=turtle.Turtle()
def star():
    t.begin_fill()
    t.color('green')
    for i in range(6):
        t.right(120)
        t.forward(80)
        t.left(60)
        t.forward(80)
        t.color('green')
        t.hideturtle()
    t.end_fill()
star()
t.up()
t.goto(100,300)
t.showturtle()

star()



turtle.mainloop()