with open(r'/Users/admin/Desktop/17968.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    if sum(line) - max(line) > 0:
        sum_ch = sum(i for i in line if i % 2 == 0)
        sum_nech = sum(i for i in line if i % 2 != 0)
        if sum_nech == sum_ch:
            cnt += 1

print(cnt)