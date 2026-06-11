with open(r'files/26_10107.txt') as file:
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]


times = sorted(times, key=lambda x: (x[1], x[0]))

ans = [times[0]]
max_break = [0, 0]
for time in times[1:]:
    if time[0] == ans[-1][1]:
        ans.append(time)
    elif time[0] > ans[-1][1]:
        max_break = [max(max_break[0], time[0] - ans[-1][1] - 1), [time[0], ans[-1][-1]]]
        ans.append(time)

print(len(ans), max_break)