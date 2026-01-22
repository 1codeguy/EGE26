def f(x):
    B = list(range(70, 81))
    for x in range(1, 1000):
        F = (x % 12 == 0) and (x in B) or (x % A != 0)
        if not F:
            return False
    return True

cnt = 0
for A in range(1, 1000):
    if f(A):
        cnt += 1
