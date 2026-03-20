from math import sqrt
def kv(x):
    return (x ** 0.5) == int(x ** 0.5)

with open(r'.\files\17_3749.txt') as file:
    data = [int(i) for i in file]

max_sqrt = max(i for i in data if kv(i)) * 3
ans = []

for num1, num2 in zip(data, data[1:]):
    u1 = sqrt(num1 * num2) == int(sqrt(num1 * num2))
    if u1:
        u2 = num1 <= max_sqrt
        u3 = num2 <= max_sqrt
        if u2 + u3 >= 1:
            ans.append(sqrt(num1 * num2))

print(len(ans), int(max(ans) + min(ans)))