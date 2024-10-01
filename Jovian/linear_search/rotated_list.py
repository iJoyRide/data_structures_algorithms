from jovian.pythondsa import evaluate_test_case

tests = [
    {'input': {'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]},'output': 3},
    {'input': {'nums': [4, 5, 6, 7, 8, 1, 2, 3]},'output': 5},
    {'input': {'nums': [1, 5, 8, 10]},'output': 0},
    {'input': {'nums': [7, 3, 5]},'output': 1},
    {'input': {'nums': []},'output': -1},
    {'input': {'nums': [5]},'output': 0}, 
]
def count_rotations(nums):    
    if not nums:
        return -1
    
    sm = nums[0] #value of the smallest number
    sm_idx = 0
    
    #find the smallest number
    for i in range(1, len(nums)):
        if nums[i] < sm:
            sm = nums[i]
            sm_idx = i
        
    #return the position/rotations of the array    
    return sm_idx

if __name__ == "__main__":
    for test in tests:
        evaluate_test_case(count_rotations, test)