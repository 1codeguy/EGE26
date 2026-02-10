def fact(num):
    d = []

    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i * i < num + 1:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]

    return d

cnt = 0
for N in range(6_086_056, 10 ** 20):
    d = fact(N)
    if len(d) == 2 and all(str(i).count('6') == 1 for i in d):
            print(N, d[1])
            cnt += 1
            if cnt == 5:
                break