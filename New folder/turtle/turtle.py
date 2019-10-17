import turtle


t = turtle.Turtle()

list1 = ['blue','purple''orange','green','red']

for i in range(200):
    t.color(i%5)
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)