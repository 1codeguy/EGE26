from random import random
x = random()
print(x)
x *= 10000
x = int(x)
res = (x % 10) + (x % 100 // 10) + (x // 100)
print(res)

