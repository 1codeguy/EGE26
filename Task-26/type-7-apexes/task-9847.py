with open(r'files\26_9847 (1).txt') as file:
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

timeline = [0] * 60 * 24
for time in times:
    for i in range(time[0], time[1]):
        timeline[i] += 1

max_cnt = max(timeline)
ans = []
for i in range(60 * 24):
    if timeline[i] == max_cnt:
        ans.append(i)

cnt = 1
for num1, num2 in zip(ans, ans[1:]):
    if num2 - num1 > 1:
        cnt += 1

print(cnt, max_cnt)
