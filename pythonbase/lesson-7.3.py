from random import randint
num = randint(0, 100)
print(num)
# if num % 3 == 0:
#     print(num / 3)
# else:
#     print(num * 2)

num /= 3 if num % 3 == 0 else 1 / 2
print(num)
