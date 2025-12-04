from itertools import product

alph = sorted('гепард')

cnt = 0
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val.count('г') == 1 and val[0] != 'а' and val[-1] != 'е':
        cnt += 1
print(cnt)