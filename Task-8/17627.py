from itertools import product
from string import printable

cnt = 0
for val in product(printable[:15], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1:
        if sum([1 for i in val if int(i, 15) > 9]) >= 2:
            cnt += 1

print(cnt)