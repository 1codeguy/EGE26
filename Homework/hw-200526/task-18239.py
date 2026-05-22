from re import finditer

with open(r'24_18239.txt') as file:
    data = file.readline()

pattern = fr'-?([1-9]+-)+[1-9]+'

matches = [match.group() for match in finditer(pattern, data)]
print(matches)

ans = 0
for match in matches:
    nums = list(map(lambda x: -int(x), match.split('-')[1:]))
    len_nums = summ = l = 0
    for r in range(len(nums)):
        summ += nums[r]
        len_nums += len(str(nums[r]))
        while summ - 2 * nums[l] <= -20_000:
            summ -= nums[l]
            len_nums -= len(str(nums[l]))
            l += 1
        ans = max(ans, len_nums)

print(ans)


    # new_match = str(nums[0])
    # l = r = 0
    # full_amount = nums[0]
    # while r < len(nums):
    #     if full_amount > -20_000:
    #         full_amount -= nums[r]
    #         new_match += '-' + str(nums[r])
    #         r += 1
    #     else:
    #         ans = max(ans, len(new_match))
    #         new_match = str(nums[l])
    #         full_amount += nums[l]
    #         l += 1