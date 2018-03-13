# version 1. I made it myself

# import turtle
#
# t = turtle.Pen()
#
# t.left(90)
# for i in range(2):
#
#     for j in range(90):
#         t.forward(1)
#         t.right(2)
#     for j in range(90):
#         t.forward(1)
#         t.left(2)


# version 2 open source code

import math
import turtle

t = turtle.Turtle()

t.pendown()
for angle in range(360):
    y = math.sin(math.radians(angle))
    scaledX = angle
    scaledY = y * 100
    t.goto(scaledX, scaledY)
t.penup()