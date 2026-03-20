with open(r'/Users/admin/Desktop/N26/26_5988.txt') as file:
    N = file.readline()
    boxes = []
    for line in file:
        size, color = line.split()
        boxes.append((int(size), color))

boxes = sorted(boxes)

