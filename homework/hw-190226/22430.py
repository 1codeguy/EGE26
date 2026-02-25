def fact(num):
    d = set()
    while num % 2 == 0:
        d |= {2}
        num //= 2

    i = 3
    while i * i <= num:
        while num % i == 0:
            d |= {i}
            num //= i
        i += 2

    if num > 2:
        d |= {num}

    if len(d) < 4:
        return []
    return d

cnt = 0
for N in range(456_789 + 1, 10 ** 20):
    if F := fact(N):
        M = F(max) + F(min)
        if M % 114 == 39:
            print(N, M)
            cnt += 1
            if cnt == 5:
                break