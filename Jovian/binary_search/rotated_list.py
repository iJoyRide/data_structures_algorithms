from jovian.pythondsa import evaluate_test_case

tests = [
    # Original Test Cases
    {
        'input': {'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14], 'target': 3},
        'output': 3
    },
    {
        'input': {'nums': [4, 5, 6, 7, 8, 1, 2, 3], 'target': 1},
        'output': 5
    },
    {
        'input': {'nums': [1, 5, 8, 10], 'target': 1},
        'output': 0
    },
    {
        'input': {'nums': [7, 3, 5], 'target': 3},
        'output': 1
    },
    {
        'input': {'nums': [], 'target': 0},  # No elements in the array
        'output': -1
    },
    {
        'input': {'nums': [5], 'target': 5},
        'output': 0
    },
    {
        'input': {'nums': [1, 2, 3, 4, 5, -1, 0], 'target': -1},
        'output': 5
    },
    
    # Additional Test Cases for Comprehensive Coverage
    {
        'input': {'nums': [4, 5, 6, 7, 0, 1, 2], 'target': 4},
        'output': 0
    },
    {
        'input': {'nums': [4, 5, 6, 7, 0, 1, 2], 'target': 2},
        'output': 6
    },
    {
        'input': {'nums': [4, 5, 6, 7, 0, 1, 2], 'target': 8},
        'output': -1
    },
    {
        'input': {'nums': [4, 5, 6, 7, 0, 1, 2], 'target': 0},
        'output': 4
    },
    {
        'input': {'nums': [4, 5, 6, 7, 0, 1, 2], 'target': 3},
        'output': -1
    },
    {
        'input': {'nums': [1, 3], 'target': 3},
        'output': 1
    },
    {
        'input': {'nums': [1, 3], 'target': 2},
        'output': -1
    },
    {
        'input': {'nums': [6, 7, 1, 2, 3, 4, 5], 'target': 1},
        'output': 2
    },
]

def count_rotations(nums, target):    
    
    # If the array is empty, immediately return -1
    if not nums:
        return -1
    
    lo = 0  # Initialize the lower bound of the search
    hi = len(nums) - 1  # Initialize the upper bound of the search
    
    while lo <= hi:
        mid = (lo + hi) // 2  # Find the middle index
        
        # Check if the middle element is the target
        if nums[mid] == target:
            return mid
        
        # Determine which side of the array is properly sorted
        if nums[lo] <= nums[mid]:
            # Left side is sorted
            # Check if the target lies within the sorted left side
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1  # Search in the left half
            else:
                lo = mid + 1  # Search in the right half
        else:
            # Right side is sorted
            # Check if the target lies within the sorted right side
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1  # Search in the right half
            else:
                hi = mid - 1  # Search in the left half
    
    # Target was not found in the array
    return -1
        
if __name__ == "__main__":
    for test in tests:
        evaluate_test_case(count_rotations, test)