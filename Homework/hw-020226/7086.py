def DEL(n, m):
    return n % m == 0

def f(x):
    B = range(50, 71)
    for x in range(1, 1000):
        F = DEL(x, A) or ((x in B) <= (not(DEL(x, 16))))
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)