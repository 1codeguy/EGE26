with open(r'files/26_9847.txt') as file:
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]


times = sorted(times, key=lambda x: (x[0], -x[1]))

apex = 0
apex_cnt = 1
midterm = [times[0]]
for time in times[1:]:
    for t in times:
        if time[1] >= t[0] and time != t:
            print(time[1], t[0])
            midterm += [t]
    if len(midterm) > apex:
        apex = len(midterm)
        apex_cnt = 1
        midterm = []
    elif len(midterm) == apex:
        apex_cnt += 1
        midterm = []

print(apex_cnt, apex)
