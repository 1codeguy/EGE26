for n in range(1, 100_000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + str(r.count('1'))
    else:
        r = '1' + r + '101'
    r = int(r, 2)
    if r > 350:
        print(n)
        break