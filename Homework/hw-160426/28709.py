def fact(num):
    d = []
    if num % 2 == 0: return 0

    i = 3
    while i * i < num + 1:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]

    if len(d) == 3:
        return d
    return []

cnt = 0
for N in range(6_300_001, 10 ** 20):
    if F := fact(N):
        if all((('3' in str(i)) + ('4' in str(i))) >= 1 for i in F):
            print(N, max(F))
            cnt += 1
            if cnt == 5:
                break