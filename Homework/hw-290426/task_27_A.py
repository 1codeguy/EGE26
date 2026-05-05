from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'/Users/admin/Downloads/Inf_1_ege2026/Доп. файлы_ИНФ/1_27_A.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'M' and data[2:] == 'III':
            stars.append(dots[-1])

cluster_1 = [d for d in dots if d[1] < 15]
cluster_2 = [d for d in dots if d[1] > 15]

clusters = [cluster_1, cluster_2]

min_center = center(min(clusters, key=len))
dists = [[dist(min_center, s), s] for s in stars]
red = min(dists, key=lambda x: (x[0], x[1]))

print(red[1][0] * 10_000, red[1][1] * 10_000)