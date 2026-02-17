from itertools import product

alph = sorted('СДАЙЕГЭ')

ans = []
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if 'ЕГЭ' in val:
        ans.append(pos)

print(sum(ans))
