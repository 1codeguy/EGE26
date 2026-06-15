from math import log2, ceil

i = ceil(log2(37))
D = 12 * 2 ** 10
for L in range(1, 100_000):
    I = ceil(L * i / 8)
    if I * 3548 > D:
        print(L)
        break