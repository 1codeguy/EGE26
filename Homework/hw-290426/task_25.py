from fnmatch import fnmatch

for N in range(89_607_090 - 89_607_090 % 9874, 10 ** 10 + 1, 9874):
    if fnmatch(str(N), '89*6?7?9?'):
        print(N, N // 9874)