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
for N in range(5_000_000 + 1, 10 ** 20):
    d = fact(N)
    if N % 100 == 12:
        min_m = 100_000
        for i in d:
            if d.count(i) == 5 and i < min_m:
                min_m = i
        if min_m != 100_000:
            print(N, min_m)
            cnt += 1
            if cnt == 5:
                break