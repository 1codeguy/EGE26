from turtle import *

m = 30
screensize(3000, 3000)
tracer(0)

for i in range(2):
    fd(5*m)
    left(90)
    bk(13*m)
    left(90)

up()
bk(10*m)
right(90)
fd(9*m)
left(90)
down()

for i in range(2):
    fd(11*m)
    right(90)
    fd(7*m)
    right(90)

up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*m,y*m)
        dot(3,'red')

update()
done()
