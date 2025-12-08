from turtle import *

screensize(3000,3000)
tracer(0)
m = 15

for i in range(2):
    fd(28*m)
    rt(90)
    fd(18*m)
    rt(90)

up()
fd(14*m)
rt(90)
fd(10*m)
lt(90)

down()
for i in range(2):
    fd(30*m)
    rt(90)
    fd(7*m)
    rt(90)

up()
for x in range(-10,30):
    for y in range(-20,10):
        goto(x*m,y*m)
        dot(3, "red")

update()
done()

