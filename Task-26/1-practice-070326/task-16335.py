with open(r'/Users/admin/Desktop/N26/26_16335.txt') as file:
    N = int(file.readline())
    cakes = [int(i) for i in file]

cakes = sorted(cakes, reverse=True)

all_cakes = [cakes[0]]

for cake in cakes:
    if all_cakes[-1] - cake >= 4:
        all_cakes.append(cake)

print(len(all_cakes), all_cakes[-1])
