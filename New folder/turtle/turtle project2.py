import turtle

def rectangle(color):
   t.begin_fill()
   t.fillcolor(color)
   for i in range(2):
       t.pensize(1)
       t.forward(200)
       t.right(90)
       t.forward(50)
       t.right(90)

   t.end_fill()
t=turtle.Turtle()

t.up()
t.pensize(5)
t.goto(0,-150)
t.down()
t.goto(0,200)
rectangle('orange')
t.goto(0,150)
rectangle('white')
t.goto(0,100)
rectangle('green')
t.forward(101)
t.color('blue')
t.circle(25)
t.left(90)
t.forward(25)
for i in range(24):
    t.forward(25)
    t.back(25)
    t.left(15)
    t.pensize(0.7)
t.hideturtle()

turtle.mainloop()
