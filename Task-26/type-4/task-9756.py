with open(r'files/26_9756.txt') as file:
    N = int(file.readline())
    events = [list(map(int, i.split())) for i in file]

events = sorted(events, key=lambda x: (x[1], x[0]))

ans = [events[0]]
for event in events[1:]:
    if ans[-1][1] <= event[0]:
        ans.append(event)

ans.remove(ans[-1])
for event in events[::-1]:
    if ans[-1][1] <= event[0]:
        ans.append(event)
        break

print(len(ans), max(ans)[1])