with open(r'files/26_8512.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    pas = []
    for line in file:
        pas.append(list(map(int, line.split())))

pas = sorted(pas)

boxes = [0] * K
cnt = last_box = 0
for p in pas:
    for i in range(K):
        if boxes[i] < p[0]:
            boxes[i] = p[1]
            cnt += 1
            last_box = i + 1
            break

print(cnt, last_box)