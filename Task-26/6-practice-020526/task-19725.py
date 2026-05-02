with open(r'/Users/admin/Desktop/N26/26_19752.txt') as file:
    N = int(file.readline())
    scores = []
    for i in file:
        data = list(map(int, i.split()))
        ans_1 = sum(data[1:])
        if ans_1 > 0:
            ans_2 = sum(i for i in data[1:] if i > 0)
            ans_3 = sum(1 for i in data[1:] if i != 0)
            scores.append([ans_1, ans_2, ans_3, data[0]])

scores = sorted(scores, key=lambda x: (-x[0], -x[1], -x[2], x[3]))

N = len(scores)
amount_stage_1 = N // 3 + sum(1 for i in scores[N // 3:] if i[:-1] == scores[N // 3 - 1][:-1])
passed_stage_1 = scores[:amount_stage_1]

N -= amount_stage_1
scores = scores[amount_stage_1:]
amount_stage_2 = N // 10 + sum(1 for i in scores[N // 10:] if i[:-1] == scores[N // 10 - 1][:-1])
passed_stage_2 = scores[:amount_stage_2]

print(scores[0], amount_stage_2)