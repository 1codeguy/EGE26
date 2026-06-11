with open(r'files/26_17537.txt') as file:
    N, M, K = map(int, file.readline().split())
    seats = [list(map(int, i.split())) for i in file]

rows = [M] * (K + 1)

for row, place in seats:
    if rows[place] > row:
        rows[place] = row - 1

max_row = max_seat = 0
for i in range(1, len(rows) - 1):
    if min(rows[i], rows[i + 1]) > max_row:
        max_row = min(rows[i], rows[i + 1])
        max_seat = i + 2

print(max_row, max_seat)