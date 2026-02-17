def f(num):
    for x in range(1, 1000):
        for y in range(1, 1000):
            F = (x ** 2 + y ** 2 > 1024 - x) or (y < -2 * x + A)
            if not F:
                return False
    return True

for A in range(1, 10 ** 6):
    if f(A):
        print(A)
        break