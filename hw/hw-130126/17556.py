def f(x):
    B = list(range(70,91))
    for x in range(1, 1000):
        F = (x % A == 0) or ((x in B) <= (not (x % 22 == 0)))
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)