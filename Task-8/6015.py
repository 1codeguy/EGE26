from string import printable as tube
from itertools import product

cnt = 0
for val in product(tube[:9], repeat=7):
    val = ''.join(val)
    if val.count('8') == 1 and val[0] != '0':
        for i in '02468':
            val = val.replace(i, '#')
        for i in '1357':
            val = val.replace(i, '+')
        if val[0] != '+' and val[-1] != '#':
            cnt += 1

print(cnt)