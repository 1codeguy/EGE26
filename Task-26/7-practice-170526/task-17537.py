with open(r'/Users/admin/Desktop/N26/26_17537.txt') as file:
    N, M, K = map(int, file.readline().split())
    seats = [M] * (K + 1)
    for i in file:
        row, seat = map(int, i.split())
        seats[seat] = min(seats[seat], row - 1)

ans = []
for seat in range(1, K + 1 - 1):
    row_1, row_2 = seats[seat:seat + 2]
    ans.append([min(row_1, row_2), seat + 1])
print(max(ans))
