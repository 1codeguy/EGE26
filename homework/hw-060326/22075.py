def DIG(x, y):
    return str(x)[0] == str(y)[0]

def f(x):
    for x in range(1, 100):
        F = (not(DIG(x, 28)) and DIG(x, 47)) <= (x > A - 20)
        if not F:
            return 0
    return 1

for A in range(1, 100):
    if f(A):
        print(A)