def f(start, cnt=0):
    if cnt == 15: return {start}
    return f(start + 10, cnt + 1) | f(start - 5, cnt + 1)

print(len(f(1)))

######################################

def f(cur, cnt=0):
    if cnt == 15:
        spots.add(cur)
        return
    f(cur + 10, cnt + 1)
    f(cur - 5, cnt + 1)

spots = set()
f(1)
print(len(spots))

######################################

dots = {1}
for i in range(15):
    dots = {x + 10 for x in dots} | {x - 5 for x in dots}
print(len(dots))