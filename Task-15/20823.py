def f(x):
    for x in range(1, 1000):
        F = (x & A == 0) <= ((77 & x == 0) and (44 & x == 0))
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)