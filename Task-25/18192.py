def is_prime(num):
    if num < 2: return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if is_prime(i): d |= {i}
            if is_prime(num // i): d |= {num // i}

    if len(d) == 3:
        return d
    return set()

cnt = 0
for N in range(1_000_001, 10 ** 8):
    if F := f(N):
        print(N, max(F))
        cnt += 1
        if cnt == 5:
            break
