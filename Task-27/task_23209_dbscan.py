from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_A_23209.txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]

# print(len(dots))
eps = 5
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    clusters += [cluster]

# print([len(cluster) for cluster in clusters])

centers = [center(cluster) for cluster in clusters]

print(max(center[0] for center in centers) * 10_000)
print(max(center[1] for center in centers) * 10_000)

from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_B_23209.txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]

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
    if len(cluster) > 1:
        clusters += [cluster]

max_center = center(max(clusters, key=len))
min_center = center(min(clusters, key=len))

print((max_center[0] - min_center[0]) * 10_000)
print(abs((max_center[1] - min_center[1]) * 10_000))
# print([len(cluster) for cluster in clusters])
