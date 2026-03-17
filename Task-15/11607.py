def DEL(n, m):
    return n % m == 0

def f(x):
    for x in range(263, 100_000):
        F = (not(DEL(x, 263) <= DEL(x, A))) and DEL(x, 71)
        if not F:
            return False
    return True

for A in range(1, 100_000):
    if not f(A):
        print(A)