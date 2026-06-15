from itertools import combinations

def f(x):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = A1 <= x <= A2
    return not A or P or Q

lineA = [13, 17, 19, 23]
lineX = [14, 18, 20]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(A2 - A1)

print(max(ans))