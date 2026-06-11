from math import dist
with open(r'files/26_9847.txt') as file:
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]


times = sorted(times)

full_time = [0] * 60 * 24 + [0]

for time in times:
    enter = time[0]
    exit = time[1]
    for i in range(time[0], time[1]):
        if enter <= i <= exit:
            full_time[i] += 1

print(full_time.count(max(full_time)), max(full_time))