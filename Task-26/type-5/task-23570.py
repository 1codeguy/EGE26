with open(r'files/26_23570 (1).txt') as file:
    N, K = map(int, file.readline().split())
    file = file.readlines()
    dachas = list(int(i) for i in file[:N])
    machines = []
    for i in file[N:]:
        machines.append(list(map(int, i.split())))

dachas = sorted(dachas)
machines = sorted(machines, key=lambda x: [x[1], -x[0]])

able = []
for d in dachas:
    for s in machines:
        if s[0] >= d:
            able.append([s[1], s[0]])
            break

print(sum(i[0] for i in able), able[-1][1])