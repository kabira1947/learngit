import turtle

t=turtle.Turtle()

list=['red','blue','orange','purple','green']

for i in range(150):
    t.color(list[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)
    t.speed(0)
    t.hideturtle()

turtle.mainloop()