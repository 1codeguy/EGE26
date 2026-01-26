def f(x):
    for x in range(1, 1000):
        for y in range(1, 1000):
            F = (78125 != (y + 4*x)) or (A > x) and (A > y)
            if not F:
                return False
    return True

for A in range(78000, 100_000):
    if f(A):
        print(A)