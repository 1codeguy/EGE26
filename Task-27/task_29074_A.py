with open(r'.\files\27_A_29074.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Z':
            stars.append(list(map(float, [x, y])))

cluster_1 = [d for d in stars if d [1] < 10]
cluster_2 = [d for d in stars if d [1] > 10]

A1 = min(len(cluster_2), len(cluster_1))
A2 = max(len(cluster_2), len(cluster_1))

print(A1, A2)
