from itertools import combinations

def f(x):
    D =  7 <= x <= 68
    C = 29 <= x <= 100
    A = A1 <= x <= A2
    return not D or C or A

lineA = [7, 29, 68, 100]
lineX = [20, 30, 70]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(A2 - A1)

print(min(ans))