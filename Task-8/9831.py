from itertools import product
from string import printable as you

cnt = 0
for val in product(you[:16], repeat=3):
    val = ''.join(val)
    if val[0] != '0' and len(set(val)) == 3:
        for i in val:
            if int(i, 16) % 2 == 0:
                val = val.replace(i, '*')
            else:
                val = val.replace(i, '#')
        if '**' not in val and '##' not in val:
            cnt += 1
print(cnt)



