from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'files/27_B_29080 (1).txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L':
            stars.append(list(map(float, [x, y])))

cluster_1 = [d for d in dots if d[1] > 23]
cluster_2 = [d for d in dots if d[1] < 23 and d[1] > 15]
cluster_3 = [d for d in dots if d[1] < 15]
stars_1 = [d for d in stars if d[1] > 23]
stars_2 = [d for d in stars if d[1] < 23 and d[1] > 15]
stars_3 = [d for d in stars if d[1] < 15]
center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

print(dist(center_1, center_3) * 10_000)

max_dist = 0
for star in stars_1:
    max_dist = max(max_dist, max(dist(star, s) for s in stars_2))
    max_dist = max(max_dist, max(dist(star, s) for s in stars_3))
for star in stars_2:
    max_dist = max(max_dist, max(dist(star, s) for s in stars_3))

print(max_dist * 10_000)