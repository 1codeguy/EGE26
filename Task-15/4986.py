def f(x):
    B = list(range(50, 71))
    for x in range(1, 1000):
        F = (x % A == 0) or (x % 23 == 0) <= (x not in B)
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)
