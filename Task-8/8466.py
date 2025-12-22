from itertools import product
from string import printable

cnt = 0
for val in product(printable[:7], repeat=6):
    val = ''. join(val)
    if val[0] != '0':
        new_val = ''
        for i in val:
            if i in '0246':
                new_val += '*'
            else:
                new_val += '+'
        for i in '0123':
            val = val.replace(i, '!')
        if val[-1] != '!' and new_val.count('*') == new_val.count('+'):
            cnt += 1
print(cnt)