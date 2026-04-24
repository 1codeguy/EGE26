from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_A_21599.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_1 = [dot for dot in dots if dot[1] > (5 / 6 * dot[0] - 10)]
cluster_2 = [dot for dot in dots if -6 < dot[1] < (5 / 6 * dot[0] - 10)]
cluster_3 = [dot for dot in dots if dot[1] < -6]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

print((center_1[0] + center_2[0] + center_3[0]) / 3 * 10_000)
print((center_1[1] + center_2[1] + center_3[1]) / 3 * 10_000)

with open(r'.\files\27_B_21599.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_1 = [dot for dot in dots if dot[1] < (-19 / 12 * dot[0] - 19)]
cluster_2 = [dot for dot in dots if dot[1] > (-19 / 12 * dot[0] - 19) and dot[0] < -10]
cluster_3 = [dot for dot in dots if dot[0] > -10 and dot[1] > (10 / 7 * dot[0] + 10)]
cluster_4 = [dot for dot in dots if dot[1] < (10 / 7 * dot[0] + 10) and dot[1] > dot[0]]
cluster_5 = [dot for dot in dots if dot[1] < dot[0] and dot[1] > -5]
cluster_6 = [dot for dot in dots if dot[1] < -5]
clusters = [cluster_6, cluster_5, cluster_4, cluster_3, cluster_2, cluster_1]

centers = [center(cluster) for cluster in clusters]

print(abs(sum(center[0] for center in centers) / len(clusters) * 10_000))
print(sum(center[1] for center in centers) / len(clusters) * 10_000)

