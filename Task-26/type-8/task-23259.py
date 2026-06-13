with open(r'files/26_15_23259.txt') as file:
    N, M = map(int, file.readline().split())
    file = [int(i) for i in file]
    pairs = file[:N]
    sleds = file[N:]

pairs = sorted(pairs)
sleds = sorted(sleds)

able = []
for p in pairs:
    for i in range(len(sleds) - 1):
        if p <= sleds[i]:
            able.append(p)
            sleds = sleds[i + 1:]
            break

for p in pairs[::-1]:
    if p <= sleds[-1]:
        able.append(p)
        break

print(len(able), max(able))