k1 = 0
for n in range(2,100_000):
    r = bin(n)[2:]
    for i in range(1, len(r), 2):
        if i == '1':
            k1 += 1

