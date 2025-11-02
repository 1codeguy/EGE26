from turtle import *

screensize(3000,3000)
tracer(0)
m = 10

for i in range(3):
    fd(7*m)
    right(90)
    fd(12*m)
    right(90)
up()

fd(4*m)
right(90)
fd(6*m)
left(90)
down()

for i in range(4):
    fd(83*m)
    right(90)
    fd(77*m)
    right(90)

up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*m,y*m)
        dot(2,"black")

update()
done()


