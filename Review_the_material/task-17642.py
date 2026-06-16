def f(num):
    d = []
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0 and i % 10 == 9 and i != 9:
            d += [i]
        elif num % (num // i) == 0 and num // i % 10 == 9 and num // i != 9:
            d += [num // i]
    if d:
        return min(d)
    return 0

cnt = 0
for N in range(800_001, 10 ** 8):
    if f(N):
        print(N, f(N))
        cnt += 1
        if cnt == 5:
            break
