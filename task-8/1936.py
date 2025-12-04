from itertools import product

cnt = 0
for val in product('пскаль', repeat=4):
    val = ''.join(val)
    if (val[0] != 'ь' and val[1] == 'ь') or (val[2] != 'ь' and val[3] == 'ь'):
        cnt += 1
    else:
        cnt += 1
print(cnt)