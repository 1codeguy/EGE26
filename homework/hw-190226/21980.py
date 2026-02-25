def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i * i <= num:
        while num % i == 0:
            if num % 10 == 7: d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]

    if not d:
        return []
    return d

cnt = 0
for N in range(750_001, 0, -1):
    if D := fact(N):
        F = sum(D) // len(D)
        if F % 111 == 0:
            print(N, F)
            cnt += 1
            if cnt == 5:
                break