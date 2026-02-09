def fact(num):
    d = []

    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i * i < num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]

    summa = sum(d)

    if len(d) == 4:
        if str(summa) == str(summa)[::-1]:
            return summa
    return 0

cnt = 0
for N in range(7_305_679, 10 ** 20):
    if F := fact(N):
        print(N, F)
        cnt += 1
        if cnt == 5:
            break
