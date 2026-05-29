def is_prime(num):
    if num < 2: return 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 0
    return 1

def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if is_prime(i):
                d |= {i}
            if is_prime(num // i):
                d |= {num // i}

    if len(d) > 1:
        return sum([max(d), min(d)])
    return 0

cnt = 0
for N in range(5_400_001, 10 ** 8):
    if F := f(N):
        if str(F) == str(F)[::-1] and F > 60_000:
            print(N, F)
            cnt += 1
            if cnt == 5:
                break