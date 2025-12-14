from itertools import product

alph = sorted('ПОЛИНА')

cnt = 0
for val in product(alph, repeat=8):
    val = ''.join(val)
    for i in val:
        if i in 'ПЛН':
            val = val.replace(i, '*')
        else:
            val = val.replace(i, '!')
    if val.count('*') > val.count('!'):
        cnt += 1
print(cnt)