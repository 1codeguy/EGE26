from itertools import product
from string import printable

bill = printable[:16]

cnt = 0
for val in product(bill, repeat=4):
    val = ''.join(val)
    for i in range(len(val) - 1):
        if val[i] == val[i + 1]:
            break
    else:
        if val[0] != '0' and val.count('3') == 1:
            cnt += 1
print(cnt)