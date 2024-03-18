nums = [1, 2, 3, 1]

map = set()

for i in nums:
    if i not in map:
        map.add(i)
    else:
        print(True)
print(False)