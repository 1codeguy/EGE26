from fnmatch import fnmatch

for N in range(123405 - 123405 % 2025, 10 ** 8 + 1, 2025):
    if fnmatch(str(N), '12*34?5'):
        print(N, N // 2025)


###############################

from string import printable
from itertools import product

# 100000000
# 1234?5

ans = []
for V in printable[:10]:
    for l in range(3):
        for Z in product(printable[:10], repeat=l):
            num = int(f'12{''.join(Z)}34{V}5')
            if num % 2025 == 0:
                ans.append([num, num // 2025])

for i in sorted(ans):
    print(*i)