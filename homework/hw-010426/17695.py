from itertools import product

cnt = 0
for num in product('0123456', repeat=5):
    num = ''.join(num)
    if num[0] != '0':
        u1 = [1 for i in num if i in '345']
        u2 = all(i1 != i2 for i1, i2 in zip(num, num[1:]))
        if len(u1) == 2 and u2:
            cnt += 1

print(cnt)