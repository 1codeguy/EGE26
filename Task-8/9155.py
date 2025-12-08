from itertools import product

alph = sorted('апрель')[::-1]

cnt = 0
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[-1] in 'ь' and pos <= 387:
        cnt += 1

print(cnt)