def uniqueOccurrences(arr):
    
    # Initialize an empty list to store the counts of occurrences
    count_list = []
    
    # Iterate over the set of unique elements in the input array
    for i in set(arr):
        # Count the occurrences of the current unique element in the original list
        count = arr.count(i)
        # Append the count to the count_list
        count_list.append(count)
        
    # Check if the count of unique elements in count_list is equal to the total count of elements in count_list
    # This checks if the number of occurrences for each unique element is itself unique
    return len(set(count_list)) == len(count_list)

    #Time: O(N)
    #Space: O(N^2)

if __name__ == "__main__":
    arr = [1, 2, 2, 1, 1, 3]
    print(uniqueOccurrences(arr))