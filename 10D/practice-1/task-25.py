def fact_3(num):
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
for N in range(6_651_221, 10 ** 10):
    if F := fact_3(N):
        if len(F) == 2 and str(F[0]).count('2') == 1 and str(F[1]).count('2') == 1:
            print(N, max(F))
            cnt += 1
            if cnt == 5:
                break