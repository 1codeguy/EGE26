from fnmatch import fnmatch

for N in range(1920368 - 1920368 % 154682, 10 ** 11 + 1, 154682):
    if fnmatch(str(N), '*192?3*68'):
        print(N, N // 154682)