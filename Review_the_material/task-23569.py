def f(num):
    d = []
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d += [i, num // i]

    if len(d) == 2:
        if str(d[0]).count('6') == 1 and str(d[1]).count('6') == 1:
            return max(d)
    return 0

cnt = 0
for N in range(6_086_056, 10 ** 8):
    if F := f(N):
        print(N, F)
        cnt += 1
        if cnt == 5:
            break