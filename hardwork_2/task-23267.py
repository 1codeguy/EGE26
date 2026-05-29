from itertools import product, repeat

alph = sorted('СТРОКА')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] not in 'АЛ' and val.count('С') == 1 and pos % 2 != 0:
        print(pos)