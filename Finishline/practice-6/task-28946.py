from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'files/27_A_28946 (1).txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]

cluster_1 = [dot for dot in dots if dot[1] < 15]
cluster_2 = [dot for dot in dots if dot[1] > 15]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

print(sum(1 for d in cluster_2 if d[1] < center_2[1]))
print(abs(center_1[0] - center_2[0]) * 10_000)


#####################################################################


with open(r'files/27_B_28946 (1).txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]

cluster_1 = [d for d in dots if d[0] > 25]
cluster_2 = [d for d in dots if d[1] > 22]
cluster_3 = [d for d in dots if d[1] < 22 and d[0] < 25]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

stars_1 = sum(1 for i in cluster_1 if center_1[0] - 0.9 <= i[0] <= center_1[0] + 0.9 and center_1[1] - 0.9 <= i[1] <= center_1[1] + 0.9)
stars_2 = sum(1 for i in cluster_2 if center_2[0] - 0.9 <= i[0] <= center_2[0] + 0.9 and center_2[1] - 0.9 <= i[1] <= center_2[1] + 0.9)
stars_3 = sum(1 for i in cluster_3 if center_3[0] - 0.9 <= i[0] <= center_3[0] + 0.9 and center_3[1] - 0.9 <= i[1] <= center_3[1] + 0.9)

print(abs(center_2[1] - center_3[1]) * 10_000)