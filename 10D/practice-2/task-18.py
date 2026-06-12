with open(r'files/18.txt') as file:
    data = [int(i) for i in file]

data = sorted(data)

cnt = 0
for i in data:
    print(i)
    cnt += 1
    if cnt == 14:
        break