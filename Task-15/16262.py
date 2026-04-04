def f(x):
    for x in range(-100, 100):
        for y in range(-100, 100):
            F = ((A < x) or (x ** 2 - 7 * x + 10 > 0)) and ((A >= y) or (y ** 2 + 7 * y + 12 > 0))
            if not F:
                return False
    return True

cnt = 0
for A in range(-100, 100):
    if f(A):
        cnt += 1

print(cnt)