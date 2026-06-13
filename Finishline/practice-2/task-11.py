from math import ceil, log2

i = ceil(log2(10 + 52 + 500))
D = 49 * 2 ** 20

for L in range(1, 10 ** 6):
    I = ceil(L * i / 8)
    if I * 45_877 > D:
        print(L)
        break