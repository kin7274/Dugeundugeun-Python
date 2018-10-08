import turtle
t=turtle.Turtle()
t.shape("turtle")
colorList=["yellow", "red", "blue", "green"]
t.fillcolor(colorList[0])
t.begin_fill()
t.circle(100)
t.end_fill()

t.fd(50)
t.fillcolor(colorList[1])
t.begin_fill()
t.circle(100)
t.end_fill()

t.fd(50)
t.fillcolor(colorList[2])
t.begin_fill()
t.circle(100)
t.end_fill()

t.fd(50)
t.fillcolor(colorList[3])
t.begin_fill()
t.circle(100)
t.end_fill()
