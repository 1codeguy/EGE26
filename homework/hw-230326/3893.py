def DEL(x, A):
    if A != 0:
        return abs(x) % A == 0

def f(x):
    for x in range(-100_000, 100_000):
        F = DEL(A, 25) and (not (DEL(x, 24) and DEL(x, 75)) or DEL(x, A))
        if not F:
            return False
    return True

cnt = 0
for A in range(-100_000, 100_000):
    if f(A):
        cnt += 1

print(cnt)