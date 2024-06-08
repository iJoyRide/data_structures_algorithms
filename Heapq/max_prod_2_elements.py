def maxProduct(nums):
    """Brute Force"""

    x = sorted(nums)

    return (x[-1] - 1) * (x[-2] - 1)


# Time complexity: O(N log N)
# Space complexity: O(N)

import heapq
def maxProductHeap(nums):
    largest = heapq.nlargest(2, nums)

    return (largest[0] - 1) * (largest[1] - 1)


# Time complexity: O(N log N)
# Space complexity: O(N)

if __name__ == "__main__":

    nums = [3, 4, 5, 2]
    print(maxProduct(nums))
    print(maxProductHeap(nums))
