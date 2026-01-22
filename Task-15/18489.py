def f(x):
    for x in range(1, 1000):
        F = ((str(x)[-1] != '5') and (str(x)[-1] == '4')) <= (x > A - 11)
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)
        