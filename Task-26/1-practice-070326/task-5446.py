with open(r'/Users/admin/Desktop/N26/26_5446.txt') as file:
    N = int(file.readline())
    tubes = [tuple(map(int, i.split())) for i in file]

tubes = sorted(tubes, key=lambda x: (-x[0] + 2 * x[1]))

all_tubes = [tubes[0]]

for tube in tubes:
    if all_tubes[-1][0] - 2 * all_tubes[-1][1] - tube[0] >= 3:
        all_tubes += [tube]

all_tubes = all_tubes[:-1]

for tube in sorted(tubes, key=lambda x: -x[0]):
    if all_tubes[-1][0] - 2 * all_tubes[-1][1] - tube[0] >= 3:
        all_tubes += [tube]
        break

print(len(all_tubes), all_tubes[-1][0])