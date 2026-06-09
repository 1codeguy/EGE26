with open(r'files/26_1207.txt') as file:
    S, N = map(int, file.readline().split())
    users = [int(i) for i in file]

users = sorted(users)

ans = []
for user in users:
    if S - user >= 0:
        ans.append(user)
        S -= user

S += ans[-1]
ans.remove(ans[-1])
for user in users[::-1]:
    if S - user >= 0:
        ans.append(user)
        break

print(len(ans), max(ans))