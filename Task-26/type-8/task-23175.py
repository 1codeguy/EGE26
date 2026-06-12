with open(r'files/26_2_23175.txt') as file:
    N, M = map(int, file.readline().split())
    file = [int(i) for i in file]
    weights = file[:N]
    conts = file[N:]

weights = sorted(weights)
conts = sorted(conts)


packed = []
for w in weights:
    for i in range(len(conts) - 1):
        if conts[i] >= w:
            packed.append(w)
            conts = conts[i + 1:]
            break

for w in weights[::-1]:
    if conts[-1] >= w:
        packed.append(w)
        break

res = packed[-1] - packed[-2]

print(len(packed), res)
