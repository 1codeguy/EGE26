def f(x):
    for x in range(1000):
        for y in range(1000):
            F = not((x < 7) or (y >= 5 * x + A - 60) or (x >= 36) or (y < 225))
            if not F:
                return False
    return True

for A in range(100_000):
    if not f(A):
        print(A)