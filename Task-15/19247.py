def f(x):
    for x in range(1, 1000):
        for y in range(1, 1000):
            F = (x - 3 * y < A) or (y > 400) or (x > 56)
            if not F:
                return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)
        break