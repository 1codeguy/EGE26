from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'/Users/admin/Desktop/N27/27A_18678.txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]

eps = 1
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) >= 30:
        clusters.append(cluster)

centers = [center(cluster) for cluster in clusters]

print(sum(center[0] for center in centers) / len(centers) * 100_000)
print(sum(center[1] for center in centers) / len(centers) * 100_000)

with open(r'/Users/admin/Desktop/N27/27B_18678.txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]

eps = 1
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) >= 30:
        clusters.append(cluster)

centers = [center(cluster) for cluster in clusters]

print(sum(center[0] for center in centers) / len(centers) * 100_000)
print(sum(center[1] for center in centers) / len(centers) * 100_000)