from itertools import product

ans = []
for val in product('0123456', repeat=5):
    if val[0] != '0':
        if val.count('6') == 1:
            flag = True
            for i in range(len(val) - 1):
                if val[i] == val[i + 1]:
                    flag = not flag
                    break
            if flag:
                ans.append(''.join(val))

print(len(ans))