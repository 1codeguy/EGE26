from turtle import *

screensize(3000, 3000)
tracer(0)
m = 15

for i in range(6):
    fd(33*m)
    rt(90)
    fd(20*m)
    rt(90)

up()
fd(3*m)
rt(90)
fd(9*m)
lt(90)

down()
for i in range(6):
    fd(24*m)
    rt(90)
    fd(25*m)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 10):
        goto(x*m, y*m)
        dot(2, 'red')

update()
done()