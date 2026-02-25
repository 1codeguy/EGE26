from fnmatch import fnmatch

for N in range(5_023_030 - 5_023_030 % 98_591, 10 ** 10 + 1, 98_591):
    if fnmatch(str(N), '5?2*3?3?'):
        print(N, N // 98591)