from string import printable as nest
from itertools import product

cnt = 0
for val in product(nest[10:16], repeat=6):
    val = ''.join(val)
    for i in 'ae':
        val = val.replace(i, '+')
    if val[0] != '+' and val[-1] != '+':
        cnt += 1

print(cnt)