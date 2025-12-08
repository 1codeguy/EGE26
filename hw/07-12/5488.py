from itertools import product

alph = sorted('ПОЛИНА')

cnt = 0
for val in product(alph, repeat=8):
    val = ''.join(val)
    New_val = ''
    for i in val:
        if i in 'ПЛН':
            New_val += '#'
        elif i in 'ОИА':
            New_val += '*'
    if New_val.count('#') > New_val.count('*'):
        cnt += 1

print(cnt)