def f(num):
    d = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i}
        if num % (num // i) == 0:
            d |= {num // i}

    if len(d) == 4:
        return d
    return {}

for N in range(178_965, 178_983):
    if F := f(N):
        print(*sorted(F, reverse=True))