
def is_prime(num):
    if num < 2: return 0
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return 0
    return 1

def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if is_prime(i): d |= {i}
            if is_prime(num // i) : d |= {num // i}

    if num > 1:
        d |= {num}
    if len(d) > 0:
        return d
    return 0

cnt = 0
for N in range(250_001, 10 ** 10):
    if f(N):
        S = sum(f(N))
        if S % 17 == 0:
            print(N, S)
            cnt += 1
            if cnt == 5:
                break
