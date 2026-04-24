with open(r'/Users/admin/Desktop/N26/26_8512.txt') as file:
    qty_boxes = int(file.readline())
    qty_men = int(file.readline())
    bags = [list(map(int, i.split())) for i in file]


cnt = 0
last_box = 0