import turtle
t=turtle.Turtle()
t.shape("turtle")

color=["yellow", "red", "blue"]

t.fillcolor(color[0])
t.begin_fill()
t.circle(100)
t.end_fill()
t.up()

t.fd(200)
t.down()
t.fillcolor(color[1])
t.begin_fill()
t.circle(100)
t.end_fill()
t.up()

t.fd(200)
t.down()
t.fillcolor(color[2])
t.begin_fill()
t.circle(100)
t.end_fill()
