from fnmatch import fnmatch

for N in range(120076 - 120076 % 1923, 10 ** 8 + 1, 1923):
    if fnmatch(str(N), '1*2??76'):
        print(N, N // 1923)