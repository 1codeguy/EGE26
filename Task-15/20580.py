def f(x):
    for x in range(1, 1000):
        for y in range(1, 1000):
            F = (9*x + y > A) or (x >= 36) or (y >= 18)
            if not F:
                return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)