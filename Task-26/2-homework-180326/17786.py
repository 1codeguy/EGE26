with open(r'/Users/admin/Desktop/N26/26_17786.txt') as file:
        data = list(map(int, file.readline().split()))
        V = data[1] * 1_000
        fruits = [int(i) for i in file]

fruits = sorted(fruits, reverse=True)

for fruit in fruits.copy():
    if 7_000 <= fruit <= 12_000:
        continue
    else:
        fruits.remove(fruit)

answer = [fruits[0]]
V = V - fruits[0]

for fruit in fruits[1:]:
    if fruit <= V:
        answer += [fruit]
        V -= fruit

print(len(answer), answer[-1])