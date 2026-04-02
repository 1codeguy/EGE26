from itertools import product

cnt = 0

for val in product('0123456', repeat=7):
    val = ''.join(val)
    if val[0] not in '035':
        u1 = '22' in val
        u2 = '44' in val
        if u1 + u2 <= 1:
            cnt += 1

print(cnt)