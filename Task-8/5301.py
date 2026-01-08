from itertools import product

alph = 'ЛЕСЯ '

cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val.count(' ') == 1:
        if val[0] != ' ' and val[-1] != ' ':
            for i in 'ЛС':
                val = val.replace(i, '*')
            for i in 'ЕЯ':
                val = val.replace(i, '+')
            if '**' not in val and '++' not in val:
                cnt += 1

print(cnt)