from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'files/27_A_29080 (1).txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[:2] == 'L3':
            stars.append(list(map(float, [x, y])))

cluster_1 = [d for d in dots if d[1] > 8]
cluster_2 = [d for d in dots if d[1] < 8]
stars_1 = [d for d in stars if d[1] > 8]
stars_2 = [d for d in stars if d[1] < 8]
center_1 = center(cluster_1)
center_2 = center(cluster_2)

print(max(dist(s, center_1) for s in stars) * 10_000)
print(max(dist(s, center_2) for s in stars) * 10_000)
