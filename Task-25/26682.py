def f(num):
    d = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}

    return d

def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i * i <= num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]

    return d

cnt = 0
for N in range(5_200_000 + 1, 10 ** 20):
    d = fact(N)
    DEL = f(N)
    if len(d) == 9 and len(DEL) % 90 == 0:
        print(N, max(d))
        cnt += 1
        if cnt == 5:
            break