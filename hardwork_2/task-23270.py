from math import *

i = ceil(log2(27 + 10))
P = ceil(12 * 2**10 / 3548)

for L in range(1, 100_000):
    I = ceil(L * i / 8)
    if I >= P:
        print(L)
        break