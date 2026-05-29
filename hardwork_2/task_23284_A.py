from math import dist
from itertools import combinations

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'files/27_A_23284.txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]

cluster_1 = [dot for dot in dots if dot[1] > 15]
cluster_2 = [dot for dot in dots if dot[1] < 15]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

print((center_1[0] + center_2[0]) * 10_000)
print((center_1[1] + center_2[1]) * 10_000)

##########################################


with open(r'files/27_B_23284.txt') as file:
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

centers = [center(cluster) for cluster in clusters]

min_dist = 10 ** 10
max_dist = 0
for c1, c2 in combinations(centers, r=2):
    min_dist = min(min_dist, dist(c1, c2))
    max_dist = max(max_dist, dist(c1, c2))

print(min_dist * 10_000)
print(max_dist * 10_000)