for N in range(1, 100_000_000):
    R = bin(N)[2:]
    if N % 5 == 0:
        R = R + bin(5)[2:]
    else:
        R = R + '1'
    if int(R, 2) % 7:
        R = R + bin(7)[2:]
    else:
        R = R + '1'
    R = int(R)
    if R < 1_855_663:
        print(N)
