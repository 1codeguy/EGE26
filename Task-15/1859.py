def f(A):
    for x in range(0, 1000):
        for y in range(0, 1000):
            F = (2 * x + y != 70) or (x < y) or (A < x)
            if not F:
                return False
    return True


for A in range(0, 100):
    if f(A):
        print(A)