with open(r'files/26_9793.txt') as file:
    N = int(file.readline())
    details_1 = []
    for i in file:
        x, y = list(map(int, i.split()))
        if min(x, y) == x:
            details_1.append([x, 0])
        else:
            details_1.append([y, 1])


details_2 = sorted(details_1)

places = [0] * N
cnt = ans = 0
for d in details_2:
    if not d[1]:
        for i in range(len(places)):
            if places[i] == 0:
                places[i] = d
                cnt += 1
                break
    else:
        for i in range(len(places) - 1, -1, -1):
            if places[i] == 0:
                places[i] = d
                break

print(details_2[-1])
ans = details_1.index(details_2[-1]) + 1

print(ans, cnt - 1)

####################################################

with open(r'..\files\26_9793.txt') as file:
    N = int(file.readline())
    pieces = []
    for pos, data in enumerate(file, start=1):
        time_1, time_2 = map(int, data.split())
        if min(time_1, time_2) == time_1:
            pieces.append([time_1, 's', pos])
        else:
            pieces.append([time_2, 'o', pos])

pieces = sorted(pieces)

last_piece = pieces[-1]
cnt = sum(1 for piece in pieces if piece[1] == 's')

print(last_piece[2], cnt - 1 if last_piece[1] == 's' else 0)
