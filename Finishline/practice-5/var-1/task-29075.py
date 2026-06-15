from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'files/27_A_29075 (1).txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[2:] == 'III':
            stars.append(list(map(float, [x, y])))

cluster_1 = [d for d in dots if d[1] < 8]
cluster_2 = [d for d in dots if d[1] > 8]
stars_1 = [d for d in stars if d[1] < 8]
stars_2 = [d for d in stars if d[1] > 8]
center_1 = center(cluster_1)
center_2 = center(cluster_2)

print(center_2[0] * 10_000, center_1[1] * 10_000)

#################################################################

with open(r'files/27_B_29075 (1).txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'J':
            stars.append(list(map(float, [x, y])))

cluster_1 = [d for d in dots if d[1] > 22]
cluster_2 = [d for d in dots if d[1] > 15 and d[1] < 22]
cluster_3 = [d for d in dots if d[1] < 15]

stars_1 = [d for d in stars if d[1] > 22]
stars_2 = [d for d in stars if d[1] > 15 and d[1] < 22]
stars_3 = [d for d in stars if d[1] < 15]

res_1 = min(dist(a, b) for a in stars_1 for b in stars_2)
res_2 = min(dist(a, b) for a in stars_1 for b in stars_3)
res_3 = min(dist(a, b) for a in stars_2 for b in stars_3)
print(min(res_1, res_2, res_3) * 10_000)

res_1 = max(dist(a, b) for a in stars_1 for b in stars_2)
res_2 = max(dist(a, b) for a in stars_1 for b in stars_3)
res_3 = max(dist(a, b) for a in stars_2 for b in stars_3)
print(max(res_1, res_2, res_3) * 10_000)
