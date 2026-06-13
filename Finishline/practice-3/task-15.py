def f(A):
    for x in range(1000):
        F = ((x & 52 != 0) and (x & 48 == 0)) <= (not(x & A == 0))
        if not F:
            return False
    return True

for A in range(1000):
    if f(A):
        print(A)
        break