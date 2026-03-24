with open(r'/Users/admin/Desktop/N26/26_12113.txt') as file:
    N = file.readline()
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)

# red_traj = [max(boxes, key=lambda x: (x % 2 != 0, x))]
# blue_traj = [max(boxes, key=lambda x: (x % 2 == 0, x))]
answer = [boxes[5]]

for box in boxes:
    if box % 2 != answer[-1] % 2:
        if answer[-1] - box >= 7:
            answer += [box]

print(len(answer), answer[-1])
