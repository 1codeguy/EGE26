from fnmatch import fnmatch

for N in range(30157 - 30157 % 2023, 10 ** 8 + 1, 2023):
    if fnmatch(str(N), '3?1*57'):
        print(N, N // 2023)