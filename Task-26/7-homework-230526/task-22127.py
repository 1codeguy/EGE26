with open(r'/Users/admin/Desktop/N26/26_22127.txt') as file:
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

times = sorted(times, key=lambda x: (x[0], x[1]))
timeline = [times[0]]
for time in times[1:]:
    if timeline[-1][0] <= time[0] <= timeline[-1][1]:
        timeline[-1][1] = max(timeline[-1][1], time[1])
    else:
        timeline.append(time)

timeline = [[0, 0]] + timeline + [[86_400_000, 86_400_000]]
ans = 0
for segment_1, segment_2 in zip(timeline, timeline[1:]):
    ans += segment_2[0] - segment_1[1] - 1

print(len(timeline) - 1, ans + 1)