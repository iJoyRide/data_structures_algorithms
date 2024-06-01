def find_unique_elements(nums1, nums2):
    """Method 1"""
    
    # Initialize empty lists to store unique elements
    list1 = []
    list2 = []

    # Iterate through each element in nums1
    for i in nums1:
        # Check if the element is not present in nums2
        if i not in nums2:
            # If not present, add it to list1
            list1.append(i)

    # Iterate through each element in nums2
    for i in nums2:
        # Check if the element is not present in nums1
        if i not in nums1:
            # If not present, add it to list2
            list2.append(i)

    # Convert lists to sets to remove duplicates and return
    return set(list1), set(list2)

#Time: O(N)
#Space: O(N+M)

def find_unique_elements2(nums1, nums2):
    """Method 3: Fastest"""
    
    set1 = set()
    set2 = set()

    for i in nums1:
        if i not in nums2:
            set1.add(i)

    for i in nums2:
        if i not in nums1:
            set2.add(i)

    return set1, set2

#Time: O(N)
#Space: O(N+M)

def find_unique_elements3(nums1, nums2):
    """Method 3"""
    
    set1 = set(nums1)
    set2 = set(nums2)

    return (set1 - set2), (set2 - set1)

if __name__ == "__main__":
    nums1 = [1,2,3] 
    nums2 = [2,4,6]

    print(find_unique_elements(nums1, nums2))
    print(find_unique_elements2(nums1, nums2))
    print(find_unique_elements3(nums1, nums2))

