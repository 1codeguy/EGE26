from math import log2, ceil

L = 257
D = 33 * 2 ** 20
for N in range(1, 100_000):
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 295_740 <= D:
        print(N)