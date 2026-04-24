from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_B_29074.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L' and data[2:] == 'V':
            stars.append(list(map(float, [x, y])))

cluster_1 = [[d for d in dots if d[1] < 15],
             [d for d in stars if d[1] < 15]]
cluster_2 = [[d for d in dots if d[1] > 15 and d[1] < 22],
             [d for d in stars if d[1] > 15 and d[1] < 22]]
cluster_3 = [[d for d in dots if d[1] > 22],
             [d for d in stars if d[1] > 22]]

dist1 = [dist(center(cluster_1[0]), s) for s in cluster_1[1]]
dist2 = [dist(center(cluster_2[0]), s) for s in cluster_2[1]]
dist3 = [dist(center(cluster_3[0]), s) for s in cluster_3[1]]

dists = dist1 + dist2 + dist3
print(min(dists) * 10_000)


dist1 = [dist(center(cluster_1[0]), s) for s in cluster_1[1]]
dist2 = [dist(center(cluster_2[0]), s) for s in cluster_2[1]]
dist3 = [dist(center(cluster_3[0]), s) for s in cluster_3[1]]

dists = dist1 + dist2 + dist3
print(max(dists) * 10_000)