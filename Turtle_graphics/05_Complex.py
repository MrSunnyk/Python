import turtle
import math

t=turtle.Turtle()
t.speed(10)
t.color('Orange')
t.fillcolor('Yellow')


t.begin_fill()
for i in range(100):
    n=20*math.sqrt(i)

    t.forward(n)
    t.left(160)
    t.forward(n)
t.end_fill()

turtle.done()