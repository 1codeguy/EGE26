from math import *

for N in range(1, 10 ** 20):
    L = 211
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 23_654 >= 3241 * 2 ** 10:
        print(N)
        break
