from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'/Users/admin/Desktop/N27/27A_18677.txt') as file:
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
    if len(cluster) > 5:
        clusters.append(cluster)

# print([len(cluster) for cluster in clusters])

ans1 = sum(center(cluster)[0] for cluster in clusters) / 2 * 100_000
ans2 = sum(center(cluster)[1] for cluster in clusters) / 2 * 100_000

print(ans1, ans2)

with open(r'/Users/admin/Desktop/N27/27B_18677.txt') as file:
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
    if len(cluster) > 5:
        clusters.append(cluster)

# print([len(cluster) for cluster in clusters])

ans1 = sum(center(cluster)[0] for cluster in clusters) / 3 * 100_000
ans2 = sum(center(cluster)[1] for cluster in clusters) / 3 * 100_000

print(ans1, ans2)
