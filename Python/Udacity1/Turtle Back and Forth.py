import turtle

t = turtle.Turtle()
t.color("lime")
t.width(3)
t.penup()
t.shape("turtle")

for step in range(2000):
    t.forward(1)
    if t.xcor() > 200:
        t.left(180)
    if t.xcor() < -200:
        t.right(180)