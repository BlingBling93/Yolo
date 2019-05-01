def twoSum(nums, target):
    r = {}
    for x in range(0, len(nums)):
        n = target - nums[x]
        if n in r:
            return [r[n], x]
        # if not in dict, add current number to avoid doubles
        r[nums[x]] = x


o = twoSum([12, 7, 11, 15, 2], 9)
print(o)