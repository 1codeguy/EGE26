for n in range(1, 100_000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '1' + r[:-2] + '10'
    else:
        r = '10' + r[2:] + '1'
    r = int(r, 2)
    if r > 202:
        print(n)
        break


