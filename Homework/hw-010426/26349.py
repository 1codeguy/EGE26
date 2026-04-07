from itertools import product

alph = sorted('СУЛАК')

for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    for i in 'УА':
        val = val.replace(i, '+')
    if val[0] in 'ЛС' and val.count('+') <= 2 and '++' not in val:
        if pos == 12368:
            print(val)