from itertools import product
from string import printable as ian

cnt = 0
for val in product(ian[:8], repeat=6):
    val = ''.join(val)
    if val[0] != '0' and val.count('3') == 0:
        if len(val) == len(set(val)):
            for i in '0246':
                val = val.replace(i, '+')
            if '++' in val:
                cnt += 1

print(cnt)

