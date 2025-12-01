from itertools import product

alph = sorted('теория')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val.count('и') >= 2 and val[0] not in 'ртя' and pos % 2 != 0:
        print(pos)