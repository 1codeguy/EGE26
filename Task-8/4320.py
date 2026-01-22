from string import printable as code
from itertools import permutations

cnt = 0
for val in permutations(code[:8], r=6):
    val = ''.join(val)
    if val[0] != '0' and int(val, 8) % 5 == 0:
        for i in '0246':
            val = val.replace(i, '+')
        for i in '1357':
            val = val.replace(i, '#')
        if '++' not in val and '##' not in val:
            cnt += 1

print(cnt)