for n in range(10_000, 100_000):
    kv = (int(min(str(n))) + int(max(str(n)))) ** 2
    pr = 1
    for i in str(n):
        if int(i) % 2 == 0:
            pr *= int(i)
    if kv < pr:
        num = str(pr) + str(kv)
    else:
        num = str(kv) + str(pr)
    if int(num) == 12116:
        print(n)
        break
