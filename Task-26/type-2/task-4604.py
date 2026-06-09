with open(r'files/26_4604.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)

amount = [boxes[0]]
for box in boxes[1:].copy():
    if amount[-1] - box >= 3:
        amount.append(box)

print(len(amount), amount[-1])