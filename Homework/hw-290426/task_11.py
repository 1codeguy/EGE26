from math import ceil

L = 257
N = 17 + 480
i = ceil(N)
I = L * i
print(I * 8_388_608 / 2 ** 23)