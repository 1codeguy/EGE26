from itertools import product

alph = sorted('ДИОНСЙ')

cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    for i in range(len(val) - 1):
        if val[i] == val[i + 1]:
            break
    else:
        if (val.count('Д') >= 1 and val.count('Н') == 0) \
            or (val.count('Д') == 0 and val.count('Н') >= 1):
            cnt += 1
print(cnt)