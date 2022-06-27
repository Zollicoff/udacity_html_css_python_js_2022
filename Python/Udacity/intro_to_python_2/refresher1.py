import turtle

def spiral(sides,turn,color,width,speed):
    t = turtle.Turtle()
    t.speed(speed)
    t.color(color)
    t.width(width)
    for n in range(sides):
        t.forward(n)
        t.right(turn)

spiral(9999,220,"purple",1,0)