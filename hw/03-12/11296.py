from itertools import product

alph = sorted('досж')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[1] not in 'жс':
        print(pos)
        break