from re import finditer

with open(r'/Users/admin/Desktop/N24/24_18239.txt') as file:
    data = file.readline()

num = r'[1-9][1-9]*'
pattern = fr'({num}-)*{num}'

matches = [match.group() for match in finditer(pattern, data)]
print(matches)
# data = '-43-53-435-5345'
ans = 0
for match in matches:
    nums = list(map(int, match.split('-')))
    new_match = str(nums[0])
    l = r = 0
    full_amount = nums[0]
    while r < len(nums):
        if full_amount > -20_000:
            full_amount -= nums[r]
            new_match += '-' + str(nums[r])
            r += 1
        else:
            ans = max(ans, len(new_match))
            new_match = str(nums[l])
            full_amount += nums[l]
            l += 1

print(ans)