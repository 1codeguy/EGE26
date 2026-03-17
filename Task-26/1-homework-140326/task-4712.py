with open(r'/Users/admin/Desktop/N26/26_4712.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)

last_box = boxes[0]
cnt = 1

for box in boxes[1:]:
    if last_box - box >= 3:
        last_box = box
        cnt += 1

print(cnt, last_box)