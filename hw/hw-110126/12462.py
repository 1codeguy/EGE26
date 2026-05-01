from string import printable
from itertools import product

cnt = 0

for val in product(printable[:16], repeat=3):
    val = ''.join(val)
    if val[0] != '0':
        for i in range(len(val) - 1):
            if int(val[i], 16) <= int(val[i + 1], 16):
                break
        else:
            cnt += 1

for val in product(printable[:16], repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        for i in range(len(val) - 1):
            if int(val[i], 16) <= int(val[i + 1], 16):
                break
        else:
            cnt += 1

print(cnt)