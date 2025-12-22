from itertools import product

alph = sorted('ПРЕСТОЛ')

cnt = 0
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    for i in 'ЕО':
        val = val.replace(i, '+')
    for i in 'ПРСТЛ':
        val = val.replace(i, '*')
    if pos % 2 != 0 and val[0] == '+' and val.count('*') <= 3:
        cnt += 1

print(cnt)