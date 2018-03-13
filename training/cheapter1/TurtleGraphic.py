import turtle
# site url :     https://opentechschool.github.io/python-beginners/ko/simple_drawing.html
t = turtle.Pen()

t.pencolor("red")

t.forward(100)

t.right(90)

t.forward(100)

t.left(30)



for i in [0,1,2]:
    t.forward(50)
    t.right(90)
t.back(50)

#거북이 모양
turtle.shape("turtle")


n = turtle.Pen()

n.back(300)
n.clear(30)


