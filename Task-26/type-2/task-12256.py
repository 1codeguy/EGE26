with open(r'files/26_12256.txt') as file:
    S, N = map(int, file.readline().split())
    boxes = [int(i) for i in file]

boxes = sorted(boxes)

space = [boxes[0]]
summ = boxes[0]
for box in boxes[1:]:
    if summ + box <= S:
        space += [box]
        summ += box

summ -= space[-1]
space.remove(space[-1])
for s in space[::-1]:
    if summ + s <= S:
        space.append(s)
        break

print(len(space), space[-1])