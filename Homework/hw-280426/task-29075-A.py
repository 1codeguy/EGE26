from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'/Users/admin/Desktop/N27/27_A_29075.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[2:] == 'III':
            stars.append(list(map(float, [x, y])))

cluster_1 = [[dot for dot in dots if dot[1] < 10],
             [dot for dot in stars if dot[1] < 10]]
cluster_2 = [[dot for dot in dots if dot[1] > 10],
             [dot for dot in stars if dot[1] > 10]]

clusters = [cluster_1, cluster_2]

min_len = min(len(cluster[1]) for cluster in clusters)
max_len = max(len(cluster[1]) for cluster in clusters)

print([center(cluster[0])[0] * 10_000 for cluster in clusters if len(cluster[1]) == min_len])
print([center(cluster[0])[1] * 10_000 for cluster in clusters if len(cluster[1]) == max_len])