from math import *

for L in range(1, 10_000):
    N = 10 + 52 + 500
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 45_877 > 49 * 2 ** 20:
        print(L)
        break