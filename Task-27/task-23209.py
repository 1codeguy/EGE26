from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_A_23209.txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]

cluster_A_1 = [d for d in dots if d[0] < 5]
cluster_A_2 = [d for d in dots if d[0] > 5]

center_A_1 = center(cluster_A_1)
center_A_2 = center(cluster_A_2)

print(max(center_A_1[0], center_A_2[0]) * 10_000)
print(max(center_A_1[1], center_A_2[1]) * 10_000)

with open(r'.\files\27_B_23209.txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]

cluster_B_1 = [d for d in dots if 5 < d[1] < 10]
cluster_B_2 = [d for d in dots if 16 < d[1] < 21]
cluster_B_3 = [d for d in dots if 21 < d[1] < 26]
clusters_B = [cluster_B_1, cluster_B_2, cluster_B_3]

max_center = center(max(clusters_B, key=len))
min_center = center(min(clusters_B, key=len))

print((max_center[0] - min_center[0]) * 10_000)
print(abs((max_center[1] - min_center[1]) * 10_000))

