def f(num):
    d = set()

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}

    if len(d) > 0: return d
    return {}

ans = []
cnt = 0
for N in range(1_350_051, 10 ** 20):
    if F := f(N):
        del_11 = [i for i in F if i % 100 == 11 and i != N and i != 11]
        if len(del_11) > 0:
            ans.append((N, min(del_11)))
            cnt += 1
            if cnt == 5:
                break

print(*ans)