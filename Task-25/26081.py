def f(num):
    for i1 in range(113, num, 226):
        for i2 in range(0, 13):
            if i1 + 3 ** i2 == num:
                return i2
    return 0

cnt = 0
for N in range(100_000, 1_000_000, 2):
    if str(N).count('0') == 0:
        if M := f(N):
            print(N, M)
            cnt += 1
            if cnt == 5:
                break
