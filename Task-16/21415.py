from sys import setrecursionlimit

def F(n):
    if n <= 5: return 1
    return n + F(n - 2)

setrecursionlimit(1100)

print(F(2126) - F(2122))

################################

F = [0] * 2200
for i in range(2200):
    if i <= 5: F[i] = 1
    else: F[i] = i + F[i - 2]
print(F[2126] - F[2122])

