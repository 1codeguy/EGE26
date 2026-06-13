from math import ceil, log2

i = ceil(log2(27))
D = 31 * 2 ** 20
for L in range(1, 10 ** 6):
    I = ceil(L * i / 8)
    if I * 7_564_230 > D:
        print(L)
        break