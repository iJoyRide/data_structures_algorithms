def findPivotIndex(nums):
    # Initialize 'left' to zero, representing the sum of elements to the left of the current index.
    left = 0

    # 'right' is initially set to the sum of all elements in the array.
    right = sum(nums)

    # Iterate over each element in the array by its index.
    for i in range(len(nums)):
        # Since the current index is part of the 'right' sum, subtract it before comparing.
        right -= nums[i]
        
        # Check if the sum of elements to the left and right of index 'i' are equal.
        if left == right:
            # Return the current index if it is the pivot index.
            return i
        
        # Add the current element to 'left' after checking, for the next iteration.
        left += nums[i]
    
    # If no pivot index is found, return -1.
    return -1
#Time: O(N)
#Space: O(1)

if __name__ == "__main__":
    nums = [1,7,3,6,5,6]
    print(findPivotIndex(nums))