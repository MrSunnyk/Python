import turtle

t = turtle.Turtle()
t.color("red")# function to specify the color you want to Outlines.
t.fillcolor("yellow") # function to specify the color you want to fill the shape with.

t.begin_fill()#This tells Turtle to remember the path you draw and fill it later.
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

t.end_fill() #This tells Turtle to fill the shape with the previously set color.

t.hideturtle()#If you don't want to see the turtle you can hide it using t.hideturtle().
turtle.done()