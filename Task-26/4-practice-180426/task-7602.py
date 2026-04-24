with open(r'/Users/admin/Desktop/N26/26_7602.txt') as file:
    qu_boxes = int(file.readline())
    qu_men = int(file.readline())
    bags = [list(map(int, i.split())) for i in file]

boxes = [0] * qu_boxes
last_box = 0
acce = 0

for time in sorted(bags):
    for i in range(qu_boxes):
        if boxes[i] < time[0]:
            boxes[i] = time[1]
            last_box = i + 1
            acce += 1
            break


print(acce, last_box)

