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

    M = max(d) + min(d)
    if M % len(set(d)) == 0 and str(M)[-2:] == '63':
        return M
    return 0

cnt = 0
for N in range(7_800_001, 10 ** 10):
    if F := fact(N):
        print(N, F)
        cnt += 1
        if cnt == 5:
            break