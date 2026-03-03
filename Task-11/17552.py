from math import *

for N in range(1, 10 ** 10):
    L = 261
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 252_000 * I > 31 * 2 ** 20:
        print(N)
        break