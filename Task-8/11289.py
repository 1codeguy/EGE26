from string import printable
from itertools import permutations

cnt = 0
for val in permutations(printable[:9], r=7):
    val = ''.join(val)
    if val[0] != '0' and val.count('2') == 0:
        for i in '02468':
            val = val.replace(i, '+')
        for i in '1357':
            val = val.replace(i, '*')
        if '**' not in val and '++' not in val:
            cnt += 1

print(cnt)