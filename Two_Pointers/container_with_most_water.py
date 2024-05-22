def maxArea(height):
    """Method 1: My method"""

    # Initialize two pointers, one at the beginning (left) and one at the end (right) of the height array
    left = 0
    right = len(height) - 1
    # Initialize a variable to keep track of the maximum amount of water
    max_amt = 0

    # Loop until the two pointers meet
    while left < right:
        # Calculate the volume of water contained between the left and right pointers
        vol = min(height[left], height[right]) * (right - left)
        
        # Update the maximum amount of water if the current volume is greater
        max_amt = max(max_amt, vol)
        
        # Move the pointer that points to the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    # Return the maximum amount of water found
    return max_amt

if __name__ == "__main__":
    # Example usage: Call the maxArea function with a sample height array
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))  # Output should be 49
