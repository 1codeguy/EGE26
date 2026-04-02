with open(r'.\files\26.txt') as file:
    N = file.readline()
    sportsmen = [list(map(int, i.split())) for i in file]

N = 9
sportsmen = [[41, 3], [43, 125], [50, 33], [42, 125], [42, 126], [42, 127], [41, 125], [50, 126], [42, 126]]
sportsmen = sorted(sportsmen, key=lambda x: (x[0], -x[1]))

large_group = []
small_group = [sportsmen[0]]


for sportsman in sportsmen.copy()[1:]:
    if sportsman[0] - small_group[-1][0] == 1:
        small_group += sportsman
        sportsmen.remove(sportsman)


print(large_group)