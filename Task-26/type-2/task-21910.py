with open(r'files/26_21910.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)

ans = [boxes[0]]
for box in boxes[1:]:
    if box + 9 <= ans[-1]:
        ans.append(box)

print(len(ans), ans[-1])