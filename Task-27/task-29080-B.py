from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_B_29080.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L':
            stars.append(list(map(float, [x, y])))

cluster_1 = [[d for d in dots if d[1] < 16],
             [d for d in stars if d[1] < 16]]
cluster_2 = [[d for d in dots if 23 > d[1] > 16],
             [d for d in stars if 23 > d[1] > 16]]
cluster_3 = [[d for d in dots if 23 < d[1]],
             [d for d in stars if 23 < d[1]]]

clusters = [cluster_1, cluster_2, cluster_3]

# print([len(cl[1]) for cl in clusters])

print(dist(center(clusters[0][0]), center(clusters[2][0])) * 10_000)

B2 = []
for s1 in cluster_1[1]:
    for s2 in cluster_2[1]:
        B2.append(dist(s1, s2))
for s1 in cluster_1[1]:
    for s3 in cluster_3[1]:
        B2.append(dist(s1, s3))
for s2 in cluster_2[1]:
    for s3 in cluster_3[1]:
        B2.append(dist(s3, s2))

print(max(B2) * 10_000)