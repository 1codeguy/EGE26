from itertools import product
from string import printable as dude

cnt = 0
for val in product(dude[:8], repeat=5):
    if val[0] != '0' and int(val[0]) % 2 == 0 \
            and val[-1] not in '26' and val.count('7') <= 2:
        cnt += 1
print(cnt)