with open(r'files/26_1868.txt') as file:
    N = int(file.readline())
    seats = [list(map(int, i.split())) for i in file]

seats.remove(seats[-1])
seats = sorted(seats, key=lambda x: (-x[0], x[1]))

row_ans = min_seat = 0
for s1, s2 in zip(seats, seats[1:]):
    if s1[0] == s2[0]:
        if s2[1] - s1[1] == 3:
            row_ans = s1[0]
            min_seat = s1[1] + 1
            break

print(row_ans, min_seat)
