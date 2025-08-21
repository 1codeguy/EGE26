num = int(input())
k = 0
for i in range(1, num + 1):
    if num % i == 0:
        k += 1
if k > 2:
    print('not simple')
else:
    print('simple')