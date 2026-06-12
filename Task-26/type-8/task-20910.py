with open(r'files/26_20910.txt') as file:
    N, M, K = map(int, file.readline().split())
    visitors = [list(map(int, i.split())) for i in file]

seats = [M] * (K + 1)

for row, place in visitors:
    if seats[place] > row:
        seats[place] = row - 1

ans = []
for i in range(1, K + 1 - 1):
    ans.append([min(seats[i], seats[i + 1]), i])

print(*max(ans, key=lambda x: (x[0], -x[1])))