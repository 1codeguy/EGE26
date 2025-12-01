from itertools import product

alph = sorted('строка')
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val.count('с') == 1 and val[1] not in 'ал' and pos % 2 != 0:
        print(pos)
