```
from fnmatch import fnmatch

def is_not_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return True
    return False

ans = []
for N in range(4, 10 ** 4):
    if is_not_prime(N):
        for M in range(22768, 10 ** 8, 22768):
            if fnmatch(str(M), f'1{N}03*6*'):
                ans.append([M, N])

ans.sort()

for s in ans:
    print(*s)
```