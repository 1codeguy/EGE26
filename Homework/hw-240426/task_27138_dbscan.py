from math import dist
from statistics import median_low


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

def new(cluster_1, clusters):
    new_clusters = []
    for cluster in clusters:
        for dot in cluster:
            new_clusters.append(dot)
    res = []
    for dot in cluster_1:
        sum_dist = sum(dist(dot, d) for d in new_clusters)
        res.append([sum_dist, dot])
    return max(res)[1]

with open(r'/Users/admin/Desktop/N27/27A_27138.txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]

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

# print([len(cluster) for cluster in clusters])

centers = [center(cluster) for cluster in clusters]


print(abs(centers[0][0] - centers[1][0]) * 10_000)
print(abs(centers[0][1] - centers[1][1]) * 10_000)

with open(r'/Users/admin/Desktop/N27/27B_27138.txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]

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

# print([len(cluster) for cluster in clusters])

jaylin = [max(dot[0] for dot in cluster) for cluster in clusters if len(cluster) % 2 != 0]

print(jaylin)

news = [new(cluster, clusters.remove(cluster)) for cluster in clusters.copy()]


for cluster in clusters.copy():
    clusters = clusters.remove(cluster)
    print(clusters)

