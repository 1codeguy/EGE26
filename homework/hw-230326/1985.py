from itertools import permutations

alph = 'АБИКОЛУН'

cnt = 0
for val in permutations(alph, r=8):
    val = ''.join(val)
    for i in 'АИОУ':
        val = val.replace(i, '#')
    for i in 'БКЛН':
        val = val.replace(i, '!')
    if '##' not in val and '!!' not in val:
        cnt += 1

print(cnt)