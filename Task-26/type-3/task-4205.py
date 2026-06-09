with open(r'files/26_4205.txt') as file:
    N = int(file.readline())
    places = [list(map(int, i.split())) for i in file]

places = sorted(places, key=lambda x: (-x[0], x[1]))

for s1, s2 in zip(places, places[1:]):
    if s1[0] == s2[0]:
        print(s1, s2)
        if s2[1] - s1[1] == 14:
            print(s2[0], s1[1] + 1)
            break
