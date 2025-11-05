from turtle import *

screensize(3000,3000)
tracer(0)
m = 20

fd(270)
for i in range(2):
    fd(8*m)
    rt(120)

right(120)
for i in range(2):
    right(120)
    fd(3*m)
    rt(240)
rt(240)

for i in range(2):
    fd(14*m)
    rt(120)

up()
for x in range(-10,50):
    for y in range(-20,10):
        goto(x*m,y*m)
        dot(3,"red")

update()
done()

