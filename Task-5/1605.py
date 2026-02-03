for N in range(1, 100_000):
        R = bin(2 + N)[2:]
        R = R + str(R.count('1') % 2)
        R = R + str(R.count('1') % 2)
        R = int(R, 2)
        if R < 61:
            print(N)