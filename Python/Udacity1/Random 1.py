import turtle
import random

t = turtle.Turtle()

t.speed(0)

for step in range(100):
    angle = random.randint(-90,90)
    color = random.choice(["red", "orange", "yellow", "green", "blue", "purple"])
    t.width(random.randint(1, 20))
    t.color(color)
    t.right(angle)
    t.forward(random.randint(1, 10))