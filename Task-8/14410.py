from itertools import product

alph = sorted('солнце')

cnt = 0
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] not in 'ое' and val.count('ц') == 2:
        cnt += 1

print(cnt)
