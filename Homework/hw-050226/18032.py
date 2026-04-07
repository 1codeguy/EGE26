def f(num):
    d = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if sum(d) % 100 == 23:
        return sum(d)
    return 0

for N in range(1_000, 10_000):
    if F := f(N):
        print(N, F)