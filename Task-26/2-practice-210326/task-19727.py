with open(r'/Users/admin/Desktop/N26/26.2_19727.txt') as file:
    M, N = map(int, file.readline().split())
    delivery = [int(i) for i in file]

delivery = sorted(delivery)
ans1 = []
for bidon in delivery:
    if sum(ans1) + bidon <= M:
        ans1.append(bidon)

free_space = M - sum(ans1[:-1])

ans2 = sum(i > free_space for i in delivery)

print(len(ans1), ans2)