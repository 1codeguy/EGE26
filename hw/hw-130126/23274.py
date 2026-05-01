def f(x):
    for x in range(1000):
        for y in range(1000):
            F = (2*x + y != 110) or (x < y) or (A < x)
            if not F:
                return False
    return True

for A in range(1000):
    if f(A):
        print(A)