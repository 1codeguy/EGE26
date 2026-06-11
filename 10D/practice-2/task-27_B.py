from math import dist

with (open(r'files/27_B_29081.txt') as file):
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data != 'VII' and int(data[1]) >= 8:
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
stars_3 = [dot for dot in clusters[2] if dot in stars]

min_dist_1 = min(dist(a, b) for a in stars_1 for b in stars_2)
min_dist_2 = min(dist(a, b) for a in stars_1 for b in stars_3)
min_dist_3 = min(dist(a, b) for a in stars_3 for b in stars_2)

print(min(min_dist_1, min_dist_2, min_dist_3) * 10_000)

mid_dist_1 = sum(dist(a, b) for a in stars_1 for b in stars_1 if a != b) / len(stars_1)
mid_dist_2 = sum(dist(a, b) for a in stars_2 for b in stars_2 if a != b) / len(stars_2)
mid_dist_3 = sum(dist(a, b) for a in stars_3 for b in stars_3 if a != b) / len(stars_3)
print((mid_dist_1 + mid_dist_2 + mid_dist_3) / 3 * 10_000)
