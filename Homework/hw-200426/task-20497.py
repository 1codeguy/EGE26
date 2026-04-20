from math import dist

def anticenter(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return max(res)[1]

with open(r'/Users/admin/Desktop/N27/27.19.A_20497 (2).txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

print(len(dots))
eps = 0.5
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 10:
        clusters.append(cluster)
print(len(clusters))

anticenters = [anticenter(cluster) for cluster in clusters]

print(abs(sum(anticenter[0] for anticenter in anticenters) / len(anticenters) * 10_000))
print(abs(sum(anticenter[1] for anticenter in anticenters) / len(anticenters) * 10_000))

with open(r'/Users/admin/Desktop/N27/27.19.B_20497.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

# print(len(dots))
eps = 2
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 10:
        clusters.append(cluster)

anticenters = [anticenter(cluster) for cluster in clusters]

print(abs(sum(anticenter[0] for anticenter in anticenters) / len(anticenters) * 10_000))
print(abs(sum(anticenter[1] for anticenter in anticenters) / len(anticenters) * 10_000))