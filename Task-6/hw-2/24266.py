from turtle import *

screensize(3000,3000)
tracer(0)
m = 15

for i in range(4):
    fd(3*m)
    rt(90)
    fd(48*m)
    rt(90)

up()
fd(27*m)
rt(90)
fd(24*m)
rt(90)

down()
for i in range(4):
    fd(29*m)
    rt(90)
    bk(18*m)
    rt(90)

up()
for x in range(-10,20):
    for y in range(-50,10):
        goto(x*m,y*m)
        dot(3,"red")

update()
done()
