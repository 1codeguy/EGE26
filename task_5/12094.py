for n in range(1, 100_000):
    r = bin(n)[2:]
    if n % 8 == 0:
        r = r + r[-2:]
    else:
        r = r + bin((n % 8) * 2)[2:]
    r = int(r, 2)
    if r > 3001:
        print(n)
        break
