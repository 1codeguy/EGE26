def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num % i}
    if len(d):
        if sum(d) // len(d) % 100 == 12:
            return sum(d) // len(d)
    return 0

cnt = 0
for N in range(770000)[::-1]:
    if A := f(N):
        print(N, A)
        cnt += 1
        if cnt == 5:
            break