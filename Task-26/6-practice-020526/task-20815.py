```
with open(r'/Users/admin/Desktop/N26/26_20815.txt') as file:
    N, S = map(int, file.readline().split())
    astronauts = []
    for i in file:
        id, e1, e2, e3, d = map(int, i.split())
        astronauts.append([e1 + e2 + e3 + d, d, id])

astronauts = sorted(astronauts, key=lambda x: (-x[0], -x[1], x[2]))

passed = astronauts[:S]
canceled = astronauts[S:]

# print(passed[-1], canceled[0])

half_score = passed[-1][0]

for p in passed[::-1]:
    if p[0] != half_score:
        print(p[2])
        break

print(sum(1 for a in astronauts if a[0] == half_score))
```