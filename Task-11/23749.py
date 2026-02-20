from math import *

for N in range(1, 10 ** 6):
    i = ceil(log2(N))
    L = 2783
    I = ceil(L * i / 8)
    if I * 3_845_647 >= 11 * 2 ** 30:
        print(N)
        break