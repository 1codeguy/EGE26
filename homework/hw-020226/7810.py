from itertools import product

alph = 'МАСЛО'

cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    for i in 'АО':
        val = val.replace(i, '+')
    if val.count('+') == 1:
        cnt += 1
        
print(cnt)