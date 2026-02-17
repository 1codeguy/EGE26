for p in range(11, 36):
    for x in range(1, 500_000):
        if int('29A1', p) + int('47771', p) + int('12A', p) == 1_000_000 + x:
            print(p)