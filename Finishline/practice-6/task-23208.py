with open(r'files/26_23208.txt') as file:
    N = int(file.readline())
    pieces_1 = []
    for i in file:
        x, y = map(int, i.split())
        if x <= y:
            pieces_1.append([x, 0])
        else:
            pieces_1.append([y, 1])

pieces_2 = sorted(pieces_1)

conveyor = [0] * (N + 1)
cnt = 0

for p in pieces_2:
    if not p[1]:
        for i in range(len(conveyor)):
            if conveyor[i] == 0:
                cnt += 1
                conveyor[i] = p
                break
    else:
        for i in range(len(conveyor) - 1, -1, -1):
            if conveyor[i] == 0:
                conveyor[i] = p
                break

print(pieces_2[-1])
ans = pieces_1.index(pieces_2[-1]) + 1

print(ans, cnt)