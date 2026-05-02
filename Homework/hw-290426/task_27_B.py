from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'/Users/admin/Downloads/Inf_1_ege2026/Доп. файлы_ИНФ/1_27_B.txt') as file:
    dots = []
    stars = []
    crz = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'K' and data[2:] == 'III':
            stars.append(dots[-1])
        if data[0] == 'G' and data[2:] == 'V':
            crz.append(dots[-1])

cluster_1 = [[d for d in dots if d[0] > 15],
             [s for s in stars if s[0] > 15]]
cluster_2 = [[d for d in dots if d[0] < 15 and d[1] > 30],
             [s for s in stars if s[0] < 15 and s[1] > 30]]
cluster_3 = [[d for d in dots if d[0] < 15 and d[1] > 30],
             [s for s in stars if s[0] < 15 and s[1] > 30]]

clusters = [cluster_2, cluster_3, cluster_1]

min_stars = min([c for c in clusters], key=lambda x: len(x[1]))
max_stars = max([c for c in clusters], key=lambda x: len(x[1]))

center_min = center(min_stars[0])
center_max = center(max_stars[0])

print(dist(center_min, center_max) * 10_000)

stars_1 = [s for s in crz if s[1] < 30]
stars_2 = [s for s in crz if s[0] < 15 and s[1] > 30]
stars_3 = [s for s in crz if s[0] > 15]

max_dist_1 = 0
for star in stars_1:
    max_dist_1 = max(max_dist_1, max(dist(star, s) for s in stars_1))
max_dist_2 = 0
for star in stars_2:
    max_dist_2 = max(max_dist_2, max(dist(star, s) for s in stars_2))
max_dist_3 = 0
for star in stars_3:
    max_dist_3 = max(max_dist_3, max(dist(star, s) for s in stars_3))

print(max(max_dist_3, max_dist_1, max_dist_2) * 10_000)