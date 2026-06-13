def is_prime(num):
    if num < 2: return 0

    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return 0
    return 1

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

    if len(d) == 2 and d[0] != d[1]:
        return d
    return False

cnt = 0
for N in range(3_700_001, 10 ** 10):
    if F := fact(N):
        if not any(is_prime(i) for i in range(F[0] + 1, F[1])):
            print(N, sum(F))
            cnt += 1
            if cnt == 5:
                break