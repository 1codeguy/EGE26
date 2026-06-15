with open(r'files/26_13101.txt') as file:
    N = int(file.readline())
    clients = [list(map(int, i.split())) for i in file]


clients = sorted(clients, key=lambda x: x[0])
windows = {1: [], 2: []}

skipped = len_w_2 = 0
for get, left, apply in clients:
    for i in range(1, 3):
        windows[i] = [end for end in windows[i] if end > get]

    if apply == 0:
        choice = 1 if len(windows[1]) <= len(windows[2]) else 2
    else:
        choice = apply

    if len(windows[choice]) >= 14:
        skipped += 1
    elif len(windows[choice]) == 0:
        finish_time = get + left
        windows[choice].append(finish_time)
        if choice == 2:
            len_w_2 += 1
    else:
        finish_time = windows[choice][-1] + left
        windows[choice].append(finish_time)
        if choice == 2:
            len_w_2 += 1

print(len_w_2, skipped)