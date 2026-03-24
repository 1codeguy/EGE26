from sys import setrecursionlimit

setrecursionlimit(9000)

def f(start, st=0):
    if st == 13:
        if start < 0: return 1
        return 0
    return f(start - 3, st + 1) + f(start * (-3), st + 1)

print(f(333))