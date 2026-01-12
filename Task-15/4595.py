def f(x):
    for x in range(1, 100):
        F = ((x % 2 == 0) <= (not (x % 3 == 0))) or (x + A >= 80)
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)
        break