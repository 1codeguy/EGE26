from itertools import combinations

def f(x):
    B = 22 <= x <= 40
    C = 32 <= x <= 50
    A = A1 <= x <= A2
    return not A <= (B == C)

line = [x + eps for x in range(22, 51) for eps in (0, 0.1, 0.9)]

ans = []
for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(min(ans))