with open(r'files/26_24.txt') as file:
    S, N = map(int, file.readline().split())
    users = [int(i) for i in file]

users = sorted(users)

amount = []
for user in users:
    if S - user >= 0:
        amount.append(user)
        S -= user

amount.remove(amount[-1])
S += amount[-1]
for user in users[::-1]:
    if S - user >= 0:
        amount.append(user)
        break

print(len(amount), amount[-1])