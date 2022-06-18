import turtle
import random

mood = random.choice(["happy", "mad", "sad", "grumpy"])

sandy = turtle.Turtle()
sandy.width(5)

if mood == "happy":
    sandy.color("yellow")
elif mood == "mad":
    sandy.color("red")
elif mood == ("sad"):
    sandy.color("blue")
elif mood == ("grumpy"):
    sandy.color("green")
else:
    sandy.color("grey")

for side in range(5):
    sandy.forward(100)
    sandy.right(144)