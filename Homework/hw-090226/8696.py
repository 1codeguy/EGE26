def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    M = sum(d)
    if is_prime(num):
        return 0
    if is_prime(M % 100_000):
        return M

cnt = 0
for N in range(1_273_547, 10 ** 20):
    if M := f(N):
        print(N, M)
        cnt += 1
        if cnt == 5:
            break