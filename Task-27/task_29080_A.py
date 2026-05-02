from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_A_29080.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L' and data[1] == '3':
            stars.append(list(map(float, [x, y])))

cluster_1 = [[d for d in dots if d[1] > 8],
             [d for d in dots if d[1] > 8]]
cluster_2 = [[d for d in dots if d[1] < 8],
             [d for d in dots if d[1] > 8]]

clusters = [cluster_1, cluster_2]

print([len(cl[0]) for cl in clusters])

center_1 = center(cluster_1[0])
center_2 = center(cluster_2[0])

print(max(dist(center_1, s) for s in stars) * 10_000)
print(max(dist(center_2, s) for s in stars) * 10_000)

