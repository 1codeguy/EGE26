def treug(n, m, k):
    return n + m > k and n + k > m and m + k > n


def f(x):
    for x in range(1, 100):
        F = not((treug(x, 11, 18) == (max(x, 5) <= 68)) and treug(x, A, 5))
        if not F:
            return False
    return True

for A in range(1, 100)[::-1]:
    if f(A):
        print(A)
        break

##################################################

def f(x):
    return not((treug(x, 11, 18) == (max(x, 5) <= 68)) and treug(x, A, 5))

for A in range(1, 100)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break