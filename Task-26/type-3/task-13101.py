with open(r'files/26_13101.txt') as file:
    N = int(file.readline())
    clients = [list(map(int, i.split())) for i in file]

clients = sorted(clients)

queue = {1: [], 2: []}
cnt = 0
skip = 0
for enter, time, ID in clients:
    for i in 1, 2:
        for client in queue[i].copy():
            if client <= enter:
                queue[i].remove(client)
                if i == 2: cnt += 1

    if not ID:
        ID = min(queue, key=lambda x: (len(queue[x]), x))

    if len(queue[ID]) >= 14:
        skip += 1
        continue
    if queue[ID]:
        queue[ID].append(queue[ID][-1] + time)
    else:
        queue[ID].append(enter + time)


print(cnt + len(queue[2]), skip)