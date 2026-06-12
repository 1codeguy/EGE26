with open(r'files/26_17881.txt') as file:
    N = int(file.readline())
    high_students = []
    low_students = []
    for i in file:
        ID, point_1, point_2, point_3, point_4 = map(int, i.split())
        points = [point_1, point_2, point_3, point_4]
        if all(p != 2 for p in points):
            points_sum = point_1 + point_2 + point_3 + point_4
            high_students.append([ID, (point_1 + point_2 + point_3 + point_4) / 4])
        elif sum(1 for p in points if p == 2) > 2:
            low_students.append([ID, (point_1 + point_2 + point_3 + point_4) / 4])


high_students = sorted(high_students, key=lambda x: (-x[1], x[0]))
low_students = sorted(low_students, key=lambda x: (-x[1], x[0]))
print(high_students[:N // 4][-1], low_students[0])

