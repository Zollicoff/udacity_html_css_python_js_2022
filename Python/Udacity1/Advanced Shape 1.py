import turtle
links = [1, 2, 3, 4, 5, 6, 7, 8]
sides = [1, 2, 3, 4, 5, 6]
weaver = turtle.Turtle()
weaver.width(5)
weaver.color('orange')
weaver.penup()
weaver.pendown()
for link in links:
    for side in sides:
        weaver.forward(69)
        weaver.right(60)
    weaver.penup()
    weaver.right(45)
    weaver.forward(20)
    weaver.pendown()
weaver.hideturtle()