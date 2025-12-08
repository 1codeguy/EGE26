from turtle import *

screensize(3000, 3000)
tracer(0)
m = 15

for i in range(2):
    fd(10*m)
    right(90)
    fd(18*m)
    right(90)

up()
fd(5*m)
right(90)
fd(7*m)
left(90)
down()

for i in range(2):
    fd(10*m)
    right(90)
    fd(7*m)
    right(90)

up()
for x in range(0, 16):
    for y in range(-20, 10):
        goto(x*m,y*m)
        dot(2, 'black')

update()
done()