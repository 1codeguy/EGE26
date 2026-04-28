from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'/Users/admin/Desktop/N27/27_B_29075.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'J':
            stars.append(list(map(float, [x, y])))

cluster_1 = [dot for dot in stars if dot[1] < 15]
cluster_2 = [dot for dot in stars if 22 > dot[1] > 15]
cluster_3 = [dot for dot in stars if dot[1] > 22]

all_dist = []
for dot in cluster_1:
    all_dist += [dist(dot, d) for d in cluster_2]
    all_dist += [dist(dot, d) for d in cluster_3]

for dot in cluster_2:
    all_dist += [dist(dot, d) for d in cluster_3]

print(min(all_dist) * 10_000)
print(max(all_dist) * 10_000)
