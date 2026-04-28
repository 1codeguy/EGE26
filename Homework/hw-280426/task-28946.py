from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'/Users/admin/Desktop/N27/27_A_28946.txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]

eps = 1
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    clusters.append(cluster)

# print([len(cluster) for cluster in clusters])

cluster_1 = clusters[0]
cluster_2 = clusters[1]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

num1 = len([dot for dot in cluster_1 if dot[1] < center_1[1]])
num2 = len([dot for dot in cluster_2 if dot[1] < center_2[1]])
num = max(num1, num2)

print(num)
print(abs(center_1[0] - center_2[0]) * 10_000)

with open(r'/Users/admin/Desktop/N27/27_B_28946.txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]

eps = 1
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    clusters.append(cluster)

# print([len(cluster) for cluster in clusters])

cluster_1 = clusters[0]
cluster_2 = clusters[1]
cluster_3 = clusters[2]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

num1 = len([dot for dot in cluster_1 if \
        center_1[0] - 0.9 < dot[0] < center_1[0] + 0.9 and
        center_1[1] - 0.9 < dot[1] < center_1[1] + 0.9])
num2 = len([dot for dot in cluster_2 if \
        center_2[0] - 0.9 < dot[0] < center_2[0] + 0.9 and
        center_2[1] - 0.9 < dot[1] < center_2[1] + 0.9])
num3 = len([dot for dot in cluster_3 if \
        center_3[0] - 0.9 < dot[0] < center_3[0] + 0.9 and
        center_3[1] - 0.9 < dot[1] < center_3[1] + 0.9])

num = min(num1, num2, num3)

print(num)
print(abs(center_1[1] - center_3[1]) * 10_000)