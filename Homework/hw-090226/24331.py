def fact(num):
    d = []

    i = 5
    while i * i < num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 10

    if num > 2:
         d += [num]

    if len(d) == 5:
        return d[4]
    return 0

cnt = 0
for N in range(13_475_125, 10 ** 20):
    if F := fact(N):
        print(N, F)
        cnt += 1
        if cnt == 5:
            break