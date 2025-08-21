from random import randint
num = randint(100, 999)
print(num)
if num % 10 == 1 or num % 10 == 3 \
    or num % 10 == 5 or num % 10 == 7:
    print(num)
elif num % 100 // 10 == 1 or num % 100 // 10 == 3 \
        or num % 100 // 10 == 5 or num % 100 // 10 == 7:
    print(num)
elif num // 100 == 1 or num // 100 == 3 \
        or num // 100 == 5 or num // 100 == 7:
    print(num)
else:
    print('Число не содержит ни одну из цифр 1,3,5 или 7')

