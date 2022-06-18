import turtle
jack = turtle.Turtle()
jack.color("yellow")
jack.speed(0)
def draw_shape(sides, length, color):
    jack.color(color)
    for side in range(sides):
        jack.forward(length)
        jack.right(360/sides)
draw_shape(4, 100, "pink")
draw_shape(7, 100, "cyan")
draw_shape(12, 100, "brown")