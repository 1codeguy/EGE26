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
for N in range(3_600_001, 10 ** 20):
    if F := fact(N):
        if all('3' in str(i) and '5' in str(i) for i in F):
            print(N, max(F))
            cnt += 1
            if cnt == 5:
                break
