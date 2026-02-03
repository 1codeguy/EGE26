from fnmatch import fnmatch

for N in range(750122 - 750122 % 8387, 10 ** 9, 8387):
    if fnmatch(str(N), '*75?122*'):
        print(N, N // 8387)