from turtle import *

screensize(3000, 3000)
tracer(0)
m = 15

for i in range(9):
    fd(27*m)
    rt(90)
    fd(30*m)
    rt(90)

up()
fd(3*m)
rt(90)
fd(6*m)
lt(90)

down()
for i in range(9):
    fd(77*m)
    rt(90)
    fd(66*m)
    rt(90)

up()
for x in range(-10, 40):
    for y in range(-40, 10):
        goto(x*m,y*m)
        dot(10, 'white')

update()
done()