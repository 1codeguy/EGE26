from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'/Users/admin/Desktop/N27/27_B_29076.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Y':
            stars.append(list(map(float, [x, y])))

cluster_1 = [[dot for dot in dots if dot[1] < 15],
             [dot for dot in stars if dot[1] < 15]]
cluster_2 = [[dot for dot in dots if 22 > dot[1] > 15],
             [dot for dot in stars if 22 > dot[1] > 15]]
cluster_3 = [[dot for dot in dots if dot[1] > 22],
             [dot for dot in stars if dot[1] > 22]]

clusters = [cluster_1, cluster_2, cluster_3]

min_len = min(len(cluster[1]) for cluster in clusters)
max_len = max(len(cluster[1]) for cluster in clusters)

c1 = [center(cluster[0]) for cluster in clusters if len(cluster[1]) == min_len]
c2 = [center(cluster[0]) for cluster in clusters if len(cluster[1]) == max_len]
print(dist(*c1, *c2) * 10_000)

all_dist = []
for cluster in clusters:
    acenter = center(cluster[0])
    for dot in cluster[1]:
        if dot != acenter:
            all_dist += [dist(dot, acenter)]

print(max(all_dist) * 10_000)