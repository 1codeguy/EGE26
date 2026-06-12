from enum import unique

with open(r'files/26_21719.txt') as file:
    N = int(file.readline())
    students = {}
    for i in file:
        ID, num = map(int, i.split())
        if ID not in students:
            students[ID] = [num]
        else:
            students[ID] += [num]


# print(max(len(i[1]) for i in students.items()))
ans = 0
brain_ID = 0
for stud in students.items():
    cnt = 1
    set_student_result = sorted(set(stud[1]))
    if len(set_student_result) > 1:
        for a, b in zip(set_student_result, set_student_result[1:]):
            if b - a == 2:
                cnt += 1
            else:
                cnt = 1
            if cnt > ans:
                ans = cnt
                brain_ID = stud[0]
            elif cnt == ans:
                brain_ID = min(stud[0], brain_ID)

print(brain_ID, ans)