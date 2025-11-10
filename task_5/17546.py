ans = []

for n in range(1, 13):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    r = int(r, 2)
    ans.append(r)
print(max(ans))
