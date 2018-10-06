# 거북이 출발
import turtle
t=turtle.Turtle()

x1=int(input("x1 : "))
y1=int(input("y1 : "))
x2=int(input("x2 : "))
y2=int(input("y2 : "))

t.up()
t.goto(x1,y1)
t.down()
t.goto(x2,y2)
t.write("두 점 사이 거리 = " + (str)(((x1-x2)**2+(y1-y2)**2)**0.5))
