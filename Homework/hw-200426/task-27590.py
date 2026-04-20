from math import dist

def anticenter(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return max(res)[1]

with open(r'/Users/admin/Desktop/N27/27A_27590.txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]

print(len(dots))
eps = 2
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    clusters.append(cluster)

max_anticenter = anticenter(max(clusters, key=len))
min_anticenter = anticenter(min(clusters, key=len))

print(abs(sum(max_anticenter) * 10_000))
print(abs(sum(min_anticenter) * 10_000))

with open(r'/Users/admin/Desktop/N27/27B_27590.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 2
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 1:
        clusters.append(cluster)

c = [0, 0]

anticenters = [[dist(anticenter(cluster), c), anticenter(cluster)] for cluster in clusters]

print(abs(max(anticenters)[1][0] * 10_000))
print(abs(min(anticenters)[1][1] * 10_000))