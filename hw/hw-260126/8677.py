from itertools import combinations

def DEL(n, m):
    return n % m == 0

def f(x):
    return DEL(x, 17) <= ((x not in B) or (A < x + 30))

for A in range(1, 200)[::-1]:
    B = range(80, 101)
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break
