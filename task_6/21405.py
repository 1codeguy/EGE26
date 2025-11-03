from turtle import *

screensize(3000,3000)
tracer(0)
m = 30

rt(30)
for i in range(3):
    rt(150)
    fd(6*m)
    rt(30)
    fd(12*m)

up()
for x in range(-20,10):
    for y in range(-10,10):
        goto(x*m,y*m)
        dot(3, "red")

update()
done()