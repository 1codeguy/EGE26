with open(r'files/26_21598.txt') as file:
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]


timeline = [0] * (60 * 24 + 1)
for t in times:
    for i in range(t[0], t[1] + 1):
        timeline[i] += 1

counter = ans_2 = 0
ans_1 = []
for a, b in zip(timeline, timeline[1:]):
    if a == b:
        counter += 1
    else:
        ans_1.append(timeline.index(a))
        counter = 0
    ans_2 = max(ans_2, counter)

print(ans_1[-2], ans_2)