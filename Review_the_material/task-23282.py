def is_prime(num):
    if num < 2: return 0

    for i in range(2, int(num **.5) + 1):
        if num % i == 0:
            return 0
    return 1

def f(num):
    d = []

    for i in range(2, int(num **.5) + 1):
        if num % i == 0 and is_prime(i):
            d += [i]
        if num % (num // i) == 0 and is_prime(num // i):
            d += [num // i]

    if len(d) >= 2:
        M = max(d) + min(d)
        if str(M) == str(M)[::-1] and M > 60_000:
            return M
    return 0

cnt = 0
for N in range(5_400_001, 10 ** 8):
    if F := f(N):
        print(N, F)
        cnt += 1
        if cnt == 5:
            break