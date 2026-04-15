from string import printable
from itertools import permutations

cnt = 0
for val in permutations(printable[:8], r=5):
    val = ''.join(val)
    if val[0] != '0' and '1' not in val:
        for i in '0246':
            val = val.replace(i, '#')
        for i in '1357':
            val = val.replace(i, '+')
        if '##' not in val and '++' not in val:
            cnt += 1

print(cnt)