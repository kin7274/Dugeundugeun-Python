import turtle
t=turtle.Turtle()

x1=int(input("큰 원의 중심x1 : "))
y1=int(input("큰 원의 중심y1 : "))
r1=int(input("큰 원의 반지름r1 : "))
x2=int(input("작은 원의 중심x2 : "))
y2=int(input("작은 원의 중심y2 : "))
r2=int(input("작은 원의 반지금r2 : "))

distance=((x1-x2)**2 + (y1-y2)**2)**0.5

t.up()
t.goto(x1, y1-r1)
t.down()
t.circle(r1)
 
t.up()
t.goto(x2, y2-r2)
t.down()
t.circle(r2)
 
if (distance + r2 < r1):
   t.write("작은 원은 큰 원 내부에 있습니다.")
elif (distance < r1 + r2):
   t.write("작은 원은 큰 원에 걸쳐 있습니다.")
else:
   t.write("작은 원은 큰 원 외부에 있습니다.")
