with open(r'..\files\24_23206.txt') as file:
    data = file.readline()

for i in '02468':
    data = data.repalce(i, ' 0')

data = data.split()

ans = 0
for line in data:
    cnt_S = line.count('S')
    if cnt_S == 35:
        ans = max(ans, len(line))
    elif cnt_S > 35:
        while cnt_S > 35:
            if line[-1] == 'S': cnt_S -= 1
            line = line[:-1]
        ans = max(ans, len(line))