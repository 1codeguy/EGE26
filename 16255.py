from string import printable as pr
from itertools import product

cnt = 0
for val in product(pr[:9], repeat=7):
    val = ''.join(val)
    if int(val[0], 9) != 0 and int(val[-1], 9) % 3 > 0 and val.count('6') >= 1:
        cnt += 1

print(cnt)