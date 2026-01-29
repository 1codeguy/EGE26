def f(x):
    for x in range(1, 1000):
        F = (x  % 128 == 0) <= ((not (x % A == 0)) <= (not (x % 80 == 0)))
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)