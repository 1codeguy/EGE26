from math import *

x = 1024
y = 768
I_1 = (1540 - 4) * 2 ** 13

for A in range(1, 100_000):
    i = ceil(log2(A))
    I_2 = x * y * i
    if I_2 == I_1:
        print(A)