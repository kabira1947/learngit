import turtle
t=turtle.Turtle()

t.color('purple')

for side in range(30):
    t.forward(10*side)
    t.right(120)
t.hideturtle()
turtle.mainloop()