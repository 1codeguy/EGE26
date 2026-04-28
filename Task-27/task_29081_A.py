from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_A_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[2:] == 'VII':
            stars.append(dots[-1])

cluster_1 = [dot for dot in dots if dot[1] < 8]
cluster_2 = [dot for dot in dots if dot[1] > 8]

stars_1 = [dot for dot in stars if dot[1] < 8]
stars_2 = [dot for dot in stars if dot[1] > 8]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

dists = []
for s in stars_1:
    dists.append(dist(center_1, s))
for s in stars_2:
    dists.append(dist(center_2, s))

print(min(dists) * 10_000)
print(max(dists) * 10_000)

##################################

cluster_1 = [[d for d in dots if d[1] < 8],
             [d for d in stars if d[1] < 8]]
cluster_2 = [[d for d in dots if d[1] > 8],
             [d for d in stars if d[1] > 8]]
clusters = [cluster_1, cluster_2]
centers = [center(cl[0]) for cl in clusters]

ans = [dist(s, centers[i]) for i in range(2) for s in clusters[i][1]]

print(min(ans) * 10_000, max(ans) * 10_000)

ans = [dist(center(cl[0]), s) for cl in clusters for s in cl[1]]

print(min(ans) * 10_000, max(ans) * 10_000)

