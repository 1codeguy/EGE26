with open(r'/Users/admin/Desktop/N26/26_7626.txt') as file:
    qty_boxes = int(file.readline())
    qty_men = int(file.readline())
    bags = [list(map(int, i.split())) for i in file]

boxes = [0] * qty_boxes
cnt = 0
last_box = 0

for bag in sorted(bags):
    for i in range(qty_boxes):
        if boxes[i] < bag[0]:
            boxes[i] = bag[1]
            cnt += 1
            last_box = i + 1
            break

print(cnt, last_box)