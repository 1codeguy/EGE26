from itertools import product

alph = sorted('СУБЛИМАЦЯ')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    for i in range(len(val)):
        if val[i] in 'УИА':
            val = val.replace(val[i], '*')
    if pos % 2 != 0 and val[-1] != 'Я':
        if (val.count('*') == 2 and 'Я' not in val) or \
                (val.count('*') == 1 and val.count('Я') == 1) or ('*' not in val and val.count('Я') == 2):
            print(pos)
