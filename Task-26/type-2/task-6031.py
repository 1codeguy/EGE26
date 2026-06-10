with open(r'files/26_6031.txt') as file:
    N = int(file.readline())
    circles = [int(i) for i in file]

circles = sorted(circles, reverse=True)

ans = [circles[0]]
for c in circles:
    if ans[-1] - c >= 6:
        ans.append(c)

print(len(ans), min(ans))