from itertools import product

alph = sorted('AРГУМЕНТ')

for pos, val in enumerate(product(alph, repeat=4), start=1):
    val = ''.join(val)
    if len(set(val)) == 4 and sorted(val) == list(val):
        print(pos)