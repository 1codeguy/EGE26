with open(r'files/26_17565.txt') as file:
    N, S = map(int, file.readline().split())
    seamen = []
    for i in file:
        idd, exam_1, exam_2, exam_3, extra_exam = i.split()
        exams = [exam_1, exam_2, exam_3]
        seamen.append([sum(map(int, exams)), int(extra_exam), int(idd)])


seamen = sorted(seamen, key=lambda x: (-x[0], -x[1], x[2]))

print(seamen[:S])
# 7600410
ans = sum(1 for s in seamen if s[0] == 154)
print(ans)