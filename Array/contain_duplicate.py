def containsDuplicate(nums):
    map = set()

    for i in nums:
        if i not in map:
            map.add(i)
        else:
            return True
    return False

nums = [1, 2, 3, 1]

result = containsDuplicate(nums)
print(result)  # Expected output: True
