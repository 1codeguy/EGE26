from itertools import product

alph = 'ничья'

cnt = 0
for val in product(alph, repeat=7):
    val = ''.join(val)
    for i in 'ия':
        val = val.replace(i, '#')
    if val.count('#') == 2 and '##' not in val:
        cnt += 1

print(cnt)