for n in range(1, 100_000):
    r = bin(n)[2:]
    if n % 5 == 0:
        r = r + r[-3:-1]
    else:
        r = r + bin((n % 5) * 5)[2:]
    r = int(r, 2)
    if r > 256:
        print(n)
        break
