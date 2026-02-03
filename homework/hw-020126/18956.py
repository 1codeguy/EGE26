from string import printable as pr

for x in pr[:15]:
    for a in range(1, 100_000_000):
        m = int(f'432{x}3', 15)
        n = int(f'86{x}86', 15)
        if (m + a) % n == 0:
            print(a)