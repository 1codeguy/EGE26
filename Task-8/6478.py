from itertools import product

alph = sorted('МОЛЬ')

cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    val = val.replace('М', '*')
    val = val.replace('Л', '*')
    if val[0] != 'Ь' and 'ЬЬ' not in val and 'ОЬ' not in val:
        cnt += 1

print(cnt)