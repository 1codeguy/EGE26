with open(r'/Users/admin/Desktop/N26/26_5066.txt') as file:
    N = int(file.readline())
    containers = [int(i) for i in file]

containers = sorted(containers, reverse=True)

store = []
while containers:
    block = [containers[0]]
    containers.remove(containers[0])
    for container in containers.copy():
        if block[-1] - container >= 7:
            block += [container]
            containers.remove(container)
    store += [len(block)]

print(len(store), max(store))