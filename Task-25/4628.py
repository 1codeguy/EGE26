from fnmatch import fnmatch

for N in range(124065 - 124065 % 161, 10 ** 8 + 1, 161):
    if fnmatch(str(N), '12*4?65'):
        print(N, N // 141)


###############################

ans = []
from itertools import product
from string import printable

for V in printable[:10]:
    for l in range(0, 3):
        for Z in product(printable[:10], repeat=l):
            num = int(f'12{''.join(Z)}4{V}65')
            if num % 161 == 0:
                ans.append([num, num // 161])

for i in sorted(ans):
    print(*i)