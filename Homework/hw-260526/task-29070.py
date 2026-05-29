from math import *

L1 = 7
L2 = 9
P1 = 384
P2 = 256
T = 7168

for N in range(1, 2000):
    i = ceil(log2(N))
    I1 = ceil(L1 * i / 8)
    I2 = ceil(L2 * i / 8)
    total = I1 * P1 + I2 * P2
    if total == T:
        print(N)
        break