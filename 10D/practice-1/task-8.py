from string import digits
from itertools import product


cnt = 0
for val in product(digits[:7], repeat=5):
    val = ''.join(val)
    if val[0] in '2468'and val[-1] not in '210' and val.count('4') <= 1:
            cnt += 1

print(cnt)