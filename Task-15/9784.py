def f(A):
    for x in range(0, 1000):
        for y in range(0, 1000):
            F = (x * y < A) or (x < y) or (9 < x)
            if not F:
                return False
    return True

for A in range(0, 1000):
    if f(A):
        print(A)