ans = []

for N in range(1, 30):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R = '10' + R[:-2] + '00'
    else:
        R = '11' + R[:-2] + '11'
    R = int(R, 2)
    ans.append(R)

print(max(ans))