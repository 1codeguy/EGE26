with open(r'/Users/admin/Desktop/N24/24_9075.txt') as file:
    data = file.readline()

for i in '13579':
    data = data.replace(i, '+')

for i in '2468':
    data = data.replace(i, '*')

for i in data:
    if i not in '+*':
        data = data.replace(i, '!')

cnt = 0
for i in range(len(data) - 1):
    if data[i:i+1] not in '+* *+':
        cnt += 1

print(cnt)