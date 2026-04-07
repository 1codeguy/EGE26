from fnmatch import fnmatch

for N in range(1232202 - 1232202 % 2024, 10 ** 10 + 1, 2024):
    if fnmatch(str(N), '1*2322?2'):
        print(N, N // 2024)