def f(A):
    for x in range(1, 200):
        for y in range(1, 200):
            F = (x < A) and (y < 3 * A) or (2 * x + y > 128)
            if not F:
                return False
    return True

for A in range(1, 200):
    if f(A):
        print(A)
        break