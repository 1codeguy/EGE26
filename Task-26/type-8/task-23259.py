with open(r'files/26_15_23259.txt') as file:
    N, M = map(int, file.readline())
    file = [int(i) for i in file]
    pairs = file[:N]
    sleds = file[N:]

for p in pairs:
    for i in range(len(sleds)):
