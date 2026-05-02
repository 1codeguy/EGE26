from itertools import product

for pos, val in enumerate(product(sorted('АПРЕЛЬ'), repeat=6)):
    val = ''.join(val)
    if pos % 2 != 0 and val[0] not in 'АЛ' and val.count('П') >= 2:
        print(pos)
        break