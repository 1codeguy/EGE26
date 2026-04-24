from math import dist

def cry(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return max(res)[1]

with open(r'.\files\27.17.A_19566.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 1
clusters =[]
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 4:
        clusters.append(cluster)

print(len(clusters))

print(abs(sum(cry(cluster)[0] for cluster in clusters) / len(clusters) * 10_000))
print(abs(sum(cry(cluster)[1] for cluster in clusters) / len(clusters) * 10_000))

with open(r'.\files\27.17.B_19566.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 1
clusters =[]
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 4:
        clusters.append(cluster)

print(len(clusters))

print(abs(sum(cry(cluster)[0] for cluster in clusters) / len(clusters) * 10_000))
print(abs(sum(cry(cluster)[1] for cluster in clusters) / len(clusters) * 10_000))
