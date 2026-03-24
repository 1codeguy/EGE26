from sys import dont_write_bytecode
from turtle import *

screensize(3000, 3000)
tracer(0)
m = 15

for i in range(2):
    fd(10 * m)
    rt(90)
    fd(20 * m)
    rt(90)

up()
bk(4 * m)
rt(90)
fd(7 * m)
lt(90)

down()
for i in range(4):
    fd(8 * m)
    lt(90)
    fd(12 * m)
    lt(90)

up()
fd(10 * m)

down()
for i in range(4):
    fd(12 * m)
    rt(90)

up()
for x in range(-10, 40):
    for y in range(-40, 10):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()