from itertools import combinations

def f(x):
    P = 1 <= x <= 39
    Q = 23 <= x <= 58
    A = A1 <= x <= A2
    return (P <= (not Q)) <= (not A)

line = [x + eps for x in range(1, 59) for eps in (0, 0.1, 0.9)]

ans = []
for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(max(ans))