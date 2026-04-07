from itertools import product
from string import printable

cnt = 0
for val in product(printable[:20], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and int(val[0], 20) + int(val[-1], 20) == 26:
        for i in val:
            if int(i, 20) % 2 == 0:
                val = val.replace(i, '+')
            else:
                val = val.replace(i, '*')
        if val == '*+*+*' or val == '+*+*+':
            cnt += 1

print(cnt)


