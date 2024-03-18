def twoSum(nums, target):
    map = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in map: 
            return [map[diff], i]
        else:
            map[nums[i]] = i

nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))
