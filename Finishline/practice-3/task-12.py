from math import ceil, log2

L = 18
i = ceil(log2(18 + 10 + 52 + 70))
I = ceil(L * i / 8)
print((100 * 2 ** 10 - I * 2000) / 2000)
