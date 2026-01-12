def f(A):
    for x in range(0, 1000):
        for y in range(0, 1000):
            F = (x + 2*y > A) or (y < x) or (x < 30)
            if not F:
                return False
    return True

for A in (89, 1000):
    if f(A):
        print(A)