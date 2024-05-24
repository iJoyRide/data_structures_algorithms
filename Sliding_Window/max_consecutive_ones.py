def longestOnes(nums, k):
    """Method 1: https://www.youtube.com/watch?v=HsGKI02yw6M"""

    # Initialise the max window length
    max_window_length = 0

    # Initialise the number of zeros counter
    num_of_zeros = 0
    n = len(nums)

    # Left and right of the window will start from zero
    left = 0
    right = 0

    # As right of the window moves through the array
    for right in range(n):

        # If the element is 0, increase the counter
        if nums[right] == 0:
            num_of_zeros += 1

        # If number of zeros is LESS THAN k, doesn't enter the loop
        # While number of zeros is NOT LESS THAN k,
        while num_of_zeros > k:

            # If the left elemnt is 0, reduce the number of zeros count
            # Before moving the left of the window
            if nums[left] == 0:
                num_of_zeros -= 1

            # Move the left of the window by 1
            left += 1

        # Window length equals right of the window minus left plus 1
        window_length = right - left + 1
        max_window_length = max(window_length, max_window_length)

    return max_window_length
#Time: O(N)
#Space: O(1)

if __name__ == "__main__":

    binary_num = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    int_flip = 2
    print(longestOnes(binary_num, int_flip))
