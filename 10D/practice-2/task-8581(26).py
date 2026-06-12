with open(r'files/26_8581.txt') as file:
    N = int(file.readline())
    K = int(file.readline())
    M = int(file.readline())
    packs = [int(i) for i in file]

packs = sorted(packs)
fridges = [M] * K

for i in range(K):
    while packs and fridges[i] > 0:
        if packs[-1] <= fridges[i]:
            fridges[i] -= packs.pop()
        elif packs[0] <= fridges[i]:
            fridges[i] -= packs.pop(0)
        else:
            break
    if not packs:
        print(i + 1, fridges[i])
        break