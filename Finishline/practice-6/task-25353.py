for x in range(1, 100_000):
    num = 3 * 27**9 + 2 * 27**6 + 27**3 - x
    cnt = 0
    while num:
        if num % 27 == 0:
            cnt += 1
        num //= 27
    if cnt == 6:
        print(x)
        break