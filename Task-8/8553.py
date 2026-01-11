from itertools import product

alph = sorted('НОРМАЛЬЕ')

norm = 0
nenorm = 0

for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[:4] == 'НОРМ':
        norm = pos
        break

for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val == 'НЕНОРМ':
        nenorm = pos
        break

print(abs(nenorm - norm) - 1)


