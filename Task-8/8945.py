from itertools import product
from string import printable as skinhead

cnt = 0
for val in product(skinhead[:12], repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        for i in range(len(val) - 1):
            if (int(val[i], 12) % 3 == 0 and int(val[i + 1], 12) % 3 == 0) or \
                    (int(val[i], 12) % 3 != 0 and int(val[i + 1], 12) % 3 != 0):
                break
        else:
            cnt += 1

print(cnt)