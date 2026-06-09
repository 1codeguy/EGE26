with open(r'files/26_3586.txt') as file:
    N = int(file.readline())
    places = [list(map(int, i.split())) for i in file]

places = sorted(places, key=lambda x: (-x[0], x[1]))

max_amount = max_row = 0
for s1, s2 in zip(places, places[1:]):
    if s1[0] == s2[0]:
        if s2[1] - s1[1] - 1 > max_amount:
            max_amount = s2[1] - s1[1] - 1
            max_row = s1[0]

print(max_row, max_amount)