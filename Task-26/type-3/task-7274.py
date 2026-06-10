with open(r'files/26_7274.txt') as file:
    N = int(file.readline())
    places = [list(map(int, i.split())) for i in file]

places = sorted(places, key=lambda x: (-x[0], x[1]))

for p1, p2 in zip(places, places[1:]):
    if p2[0] == p1[0]:
        if p2[1] - p1[1] == 14:
            print(p2[0], p1[1] + 1)
            break