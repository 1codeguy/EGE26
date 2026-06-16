def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            F = (x > A) or (y > A) or (x + 2 * y < 80)
            if not F:
                return 0
    return 1

for A in range(0, 1000):
    if f(A):
        print(A)