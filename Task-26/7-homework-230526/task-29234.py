with open(r'/Users/admin/Desktop/N26/26_29234.txt') as file:
     K = int(file.readline())
     N = int(file.readline())
     times = []
     for line in file:
         time = list(map(int, line.split()))
         times.append(time)

times = sorted(times)

comps = [0] * K
profits = [0] * K
clients = 0

for time in times:
    for i in range(K):
        if time[0] > comps[i]:
            comps[i] = time[1]
            clients += 1
            t = time[1] - time[0]
            profits[i] += t * (t + 1) // 2
            break

print(clients, max(profits))