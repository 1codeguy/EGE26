with open(r'/Users/admin/Desktop/N26/26_9756.txt') as file:
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

times = sorted(times, key=lambda x: (x[1], x[0]))

events = [times[0]]
for time in times:
    if time[0] >= events[-1][1]:
        events.append(time)


last_event = events.pop()
for time in times[::-1]:
    if time[0] >= events[-1][1]:
        events.append(time)

print(len(events), events[-1])
