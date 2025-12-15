from string import printable
from itertools import product

cnt = 0
for val in product('0123456789AB', repeat=7):
    val = ''.join(val)
    if val[0] != '0' and val.count('B') == 2:
        for i in range(len(val) - 1):
            if int(val[i], 12) % 2 == int(val[i + 1], 12) % 2:
                break
        else:
            cnt += 1

print(cnt)