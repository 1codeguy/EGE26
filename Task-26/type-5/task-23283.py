with open(r'files/26_23283.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

times = sorted(times, key=lambda x: (x[0], x[1]))

clients = []
windows = [0] * (K + 1)
for t in times:
    for i in range(1, len(windows)):
        if t[0] >= windows[i] + 1:
            windows[i] = t[1]
            clients.append([t[1], i])
            break

print(len(clients), clients[-10:])