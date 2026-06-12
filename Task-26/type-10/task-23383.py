with open(r'files/26_23383.txt') as file:
    N = int(file.readline())
    dots = {}
    for i in file:
        ID, num = map(int, i.split())
        if num not in dots:
            dots[num] = [ID]
        else:
            dots[num] += [ID]

moda = ans = 0
for p in dots.items():
    cnt = 1
    set_p_result = sorted(set(p[1]))
    if len(set(p[1])) > 1:
        for a, b in zip(set_p_result, set_p_result[1:]):
            if b - a == 1:
                cnt += 1
            else:
                cnt = 1
            if cnt > ans:
                ans = cnt
                moda = p[0]
            elif cnt == ans:
                moda = min(p[0], moda)

print(ans, moda)