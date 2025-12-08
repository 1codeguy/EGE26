import turtle
from turtle import *

screensize(3000,3000)
tracer(0)
m = 6

for i in range(4):
    fd(19*m)
    right(90)
    fd(30*m)
    right(90)
up()

fd(2*m)
right(90)
fd(8*m)
left(90)
down()

for i in range(4):
    fd(93*m)
    right(90)
    fd(97*m)
    right(90)

up()
for x in range(-100,100):
    for y in range(-120,120):
        goto(x*m,y*m)
        dot(2,"red")
update()
done()
