
def fact(num):
    d = set()

    while num % 2 == 0:
        d.add(2)
        num //= 2

    i = 3
    while i * i <= num:
        while num % i == 0:
            d.add(i)
            num //= i
        i += 2

    if num >= 2:
        d.add(num)

    if len(d) >= 2:
        return d
    return set()

cnt = 0
for N in range(3_333_338, 10 ** 20):
    F = fact(N)
    if len(F) >= 2:
        R = max(F) - min(F)
        if R % 3 == 0 and R > 1000:
            print(N, R)
            cnt += 1
            if cnt == 5:
                break
