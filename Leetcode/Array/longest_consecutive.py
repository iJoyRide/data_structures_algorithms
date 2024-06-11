def longestConsecutive(nums):
    numset = set(nums)
    longest = 0

    for num in numset:
        if (num - 1) not in numset:
            length = 1
            while (num + length) in numset:
                length += 1
            longest = max(length, longest)
    return longest

# Time: O(N)
# Space: O(N)

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(longestConsecutive(nums))
