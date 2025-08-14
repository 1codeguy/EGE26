import random as r
num = int(input())
num1 = r.randint(0,num)
print(num1)
num1 /= 9
num1 *= 1000
num1 //= 1000
print(num1)


