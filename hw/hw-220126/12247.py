def f(x):
    for x in range(1, 1000):
        F = (x & A == 0) or (not (x & 37 == 0)) or (not (x & 12 == 0))
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)