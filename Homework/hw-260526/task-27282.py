from itertools import product
from string import printable as skinhead

alph = '0123456789ABC'

cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if val[0] != '0':
        for i in 'ABC': val = val.replace(i, '*')
        if '**' in val and val.count('*') == 2 and val.count('0') >= 2:
            cnt += 1

print(cnt)

#####################

from itertools import *

alph = '0123456789ABC'
cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if val[0] != '0':
        for i in 'ABC': val = val.replace(i, '*')
        if '**' in val and val.count('*') == 2 and val.count('0') >= 2:
            cnt += 1
print(cnt)