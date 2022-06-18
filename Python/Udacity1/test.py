import turtle

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

terry = turtle.Turtle
terry.width(10)

for sides in rainbow:
    terry.forward(100)
    terry.right(60)
