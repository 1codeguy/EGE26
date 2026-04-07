from itertools import product
from string import printable as skinhead

cnt = 0
for val in product(skinhead[:25], repeat=4):
    val = ''.join(val)
    if val[0] != '0':
        if any(i for i in val if int(i, 25) % 2 == 0):
            bol = sum(1 for i in val if int(i, 25) > 15)
            if bol > 2:
                cnt += 1

print(cnt)