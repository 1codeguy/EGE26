from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'files/27_B_29080.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L':
            stars.append(list(map(float, [x, y])))

cluster_1 = [dot for dot in dots if dot[1] > 22]
cluster_2 = [dot for dot in dots if dot[1] < 22 and dot[1] > 15]
cluster_3 = [dot for dot in dots if dot[1] < 15]

stars_1 = [star for star in stars if star[1] > 22]
stars_2 = [star for star in stars if star[1] < 22 and star[1] > 15]
stars_3 = [star for star in stars if star[1] < 15]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

print(max(len(stars_1), len(stars_2), len(stars_3)))
print(min(len(stars_1), len(stars_2), len(stars_3)))
print(len(stars_1), len(stars_2), len(stars_3))

print(dist(center_1, center_3) * 10_000)

ans_1 = max(dist(s_1, s_2) for s_1 in stars_1 for s_2 in stars_2) * 10_000
ans_2 = max(dist(s_1, s_3) for s_1 in stars_1 for s_3 in stars_3) * 10_000
ans_3 = max(dist(s_2, s_3) for s_2 in stars_2 for s_3 in stars_3) * 10_000
print(max(ans_1, ans_3, ans_2))