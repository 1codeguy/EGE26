from string import printable as skinhead
from itertools import product

cnt = 0
for val in product(skinhead[:25], repeat=4):
    val = ''.join(val)
    if val[0] != '0':
        cnt_nch = 0
        cnt_5 = 0
        for i in val:
            if int(i, 25) % 2 != 0:
                cnt_nch += 1
            if int(i, 25) <= 5:
                cnt_5 += 1
        if cnt_nch == 1 and cnt_5 <= 2:
            cnt += 1

print(cnt)