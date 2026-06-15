from math import log2, ceil

L = 172
D = 54 * 2 ** 20
for N in range(1, 100_000):
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 356_984 >= D:
        print(N)
        break