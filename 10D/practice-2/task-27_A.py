from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'files/27_A_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data == 'VII':
            stars.append(list(map(float, [x, y])))

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

stars_1 = [dot for dot in clusters[0] if dot in stars]
stars_2 = [dot for dot in clusters[1] if dot in stars]

centers = [center(cl) for cl in clusters]

min_dist_1 = min(dist(centers[0], s) for s in stars_1)
min_dist_2 = min(dist(centers[1], s) for s in stars_2)
print(min(min_dist_1, min_dist_2) * 10_000)

min_dist_1 = max(dist(centers[0], s) for s in stars_1)
min_dist_2 = max(dist(centers[1], s) for s in stars_2)
print(max(min_dist_1, min_dist_2) * 10_000)