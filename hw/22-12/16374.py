from itertools import product

cnt = 0
for val in product('0123456', repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        for i in val:
            if int(i, 7) % 2 == 0:
                val = val.replace(i, '+')
        if val.count('+') == 2:
            cnt += 1
print(cnt)