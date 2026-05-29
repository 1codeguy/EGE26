from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'files/27_A_29080.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[:2] == 'L3':
            stars.append(list(map(float, [x, y])))


cluster_1 = [dot for dot in dots if dot[1] < 8]
cluster_2 = [dot for dot in dots if dot[1] > 8]

stars_1 = [star for star in stars if star[1] < 8]
stars_2 = [star for star in stars if star[1] > 8]

center_1 = center(cluster_1)
center_2 = center(cluster_2)


# print(min(len(cluster_1), len(cluster_2)))
# print(len(cluster_1))

print(max(dist(s, center_2) for s in stars) * 10_000)
print(max(dist(s, center_1) for s in stars) * 10_000)