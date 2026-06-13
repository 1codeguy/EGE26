from sys import setrecursionlimit

setrecursionlimit(3000)

def F(n):
    if n == 1: return 1
    return n * F(n - 1)

print((F(2024) - 5 * F(2023)) / F(2022))