from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_A_28766.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Y' and data[2:] == 'III':
            stars.append(list(map(float, [x, y])))

cluster_1 = [d for d in dots if d[1] > 8]
cluster_2 = [d for d in dots if d[1] < 8]

clusters = [cluster_1, cluster_2]

min_dist = min(dist(center(min(clusters, key=len)), star) for star in stars)
max_dist = max(dist(center(min(clusters, key=len)), star) for star in stars)

print(min_dist * 10_000)
print(max_dist * 10_000)