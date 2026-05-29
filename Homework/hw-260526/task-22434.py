def f(A):
    for x in range(1, 100):
        for y in range(1, 100):
            F = (x**2 <= 136) or (y < 4*x + A - 70) or (2*y > 51)
            if not F:
                return False
    return True

for A in range(1, 100):
    if f(A):
        print(A)
        break