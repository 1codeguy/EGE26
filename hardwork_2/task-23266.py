from math import *
I_1 = 2560 * 1440 * ceil(log2(2 ** 22)) * 130
I_2 = 1920 * 1080 * 20 * 130
print((I_1 - I_2) / 2 ** 13)