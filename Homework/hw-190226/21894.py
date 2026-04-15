from string import printable
from itertools import permutations

cnt = 0
for val in set(permutations(printable[:10], r=4)):
    val = ''.join(val)
    for i in '02468':
        val = val.replace(i, '+')
    for i in '13579':
        val.replace(i, '#')
    if '##' not in val and '++' not in val:
        cnt += 1

print(cnt)