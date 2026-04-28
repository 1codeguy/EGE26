import statistics

with open(r'/Users/admin/Desktop/N26/26_18541.txt') as file:
    N, M = list(map(int, file.readline().split()))
    data = [int(i) for i in file]

weights = sorted(data[:N], reverse=True)
athletes = sorted(data[N:], reverse=True)

lifted_weights = []
for a in athletes:
    for w in weights:
        if a >= w:
            lifted_weights.append(w)
            break

print(sum(ath for ath in lifted_weights) / len(lifted_weights))
print(max(lifted_weights, key=lambda x: lifted_weights.count(x)))
