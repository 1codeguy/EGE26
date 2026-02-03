from itertools import product

alph = sorted('КАТЕР')

ans =[]
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val == 'КАРЕТА':
        ans.append(-pos)
    elif val == 'РАКЕТА':
        ans.append(pos)

print(sum(ans) - 1)