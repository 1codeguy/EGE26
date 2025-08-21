from math import pi
num = int(input())
if num == 1:
    r = int(input())
    print(pi * r ** 2)
elif num == 2:
    o1 = int(input())
    o2 = int(input())
    print(pi * o1 * o2)
else:
    print('ERROR')
