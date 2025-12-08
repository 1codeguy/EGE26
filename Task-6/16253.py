from turtle import *

screensize(10000,10000)
tracer(0)
m = 20

rt(45)
for i in range(10):
    rt(45)
    fd(203*m)
    rt(45)

up()
bk(40*m)
rt(45)

down()
for i in range(5):
    fd(20*m)
    lt(90)

up()
for x in range(-200,-100):
    for y in range(-300,-200):
        goto(x*m,y*m)
        dot(3,"red")

update()
done()