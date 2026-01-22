def f(x):
    B = list(range(20, 81))
    for x in range(1, 1000):
        F = (x in B) <= ((x % 17 == 0) <= (x == A))
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)