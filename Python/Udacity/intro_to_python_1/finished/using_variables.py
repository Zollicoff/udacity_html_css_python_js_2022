import turtle
mary = turtle.Turtle()
color = "purple"
sides = [1, 2, 3, 4, 5]
distance = 100
angle = 72
mary.color(color)
for side in sides:
    mary.forward(distance)
    mary.right(angle)