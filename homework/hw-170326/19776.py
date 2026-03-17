def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if is_prime(i): d |= {i}
            if is_prime(num // i): d |= {num // i}

    if len(d) > 1:
        return min(d) + max(d)
    return 0

cnt = 0
for N in range(23_600_001, 10 ** 20):
    M = f(N)
    if M % 213 == 171:
        print(N, M)
        cnt += 1
        if cnt == 6:
            break