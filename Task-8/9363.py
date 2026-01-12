from itertools import permutations

alph = 'ХОЧУНАБЮДЖЕТ'

cnt = 0
for val in permutations(alph):
    val = ''.join(val)
    for i in 'ОУАЮЕ':
        val = val.replace(i, '+')
    if '+++++' not in val:
        cnt += 1

print(cnt)