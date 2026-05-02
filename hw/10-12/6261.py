from string import printable
from itertools import product

cnt = 0
for val in product(printable[:8], repeat=10):
    val = ''.join(val)
    if val[0] != 0 and val.count('7') == 5 and '17' not in val \
            and '71' not in val and '37' not in val and '73' not in val \
            and '57' not in val and '75' not in val and '77' not in val:
        print(val)
        cnt += 1
print(cnt)