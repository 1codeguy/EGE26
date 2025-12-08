from turtle import *

screensize(3000,3000)
tracer(0)
m = 10

for i in range(9):
    fd(22*m)
    right(90)
    fd(6*m)
    right(90)
up()

fd(1*m)
right(90)
fd(5*m)
left(90)
down()

for i in range(9):
    fd(53*m)
    right(90)
    fd(75*m)
    right(90)

up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*m,y*m)
        dot(2,"red")

update()
done()


