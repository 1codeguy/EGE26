from turtle import *

screensize(3000,3000)
tracer(0)
m = 15

for i in range(2):
    fd(20*m)
    lt(270)
    fd(12*m)
    rt(90)

up()
fd(9*m)
rt(90)
fd(7*m)
lt(90)

down()
for i in range(2):
    fd(13*m)
    rt(90)
    fd(6*m)
    rt(90)

up()
for x in range(-10,30):
    for y in range(-15,10):
        goto(x*m,y*m)
        dot(3,"red")

update()
done()