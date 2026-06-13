from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'files/27_A_29077.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data == 'N9I':
            stars.append(list(map(float, [x, y])))


cluster_1 = [d for d in dots if d[1] < 8]
cluster_2 = [d for d in dots if d[1] > 8]

stars_2 = [d for d in stars if d[1] > 8]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

res_1 = min(dist(s, center_2) for s in stars_2)
res_2 = max(dist(s, center_1) for s in stars_2)

print(res_1 * 10_000, res_2 * 10_000)

#############################################################

with open(r'files/27_B_29077.txt') as file:
    dots = []
    huge_stars = []
    small_stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data != 'VII':
            if int(data[1]) > 7:
                huge_stars.append(list(map(float, [x, y])))
            if int(data[1]) < 4:
                small_stars.append(list(map(float, [x, y])))

cluster_1 = [d for d in dots if d[1] > 22]
cluster_2 = [d for d in dots if d[1] > 15 and d[1] < 22]
cluster_3 = [d for d in dots if d[1] < 15]

huge_stars_3 = [d for d in huge_stars if d[1] < 15]
small_stars_2 = [d for d in small_stars if d[1] > 15 and d[1] < 22]

print(len(huge_stars_3), len(small_stars_2))