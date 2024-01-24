def binary_search(list, target):
    """
    Performs a binary search for the target in the sorted list.

    Args:
    list: The sorted list in which to search for the target.
    target: The target value to search for.

    Returns:
    int: The index of the target if found, else None.
    """
    first = 0
    last = len(list) - 1  # Set last to the last index of the list

    while first <= last:
        midpoint = (first + last) // 2  # Calculate the midpoint

        if list[midpoint] == target:
            # If the target is at the midpoint, return this index
            return midpoint
        elif list[midpoint] < target:
            # If the target is greater, ignore the left half
            first = midpoint + 1
        else:
            # If the target is smaller, ignore the right half
            last = midpoint - 1  # Corrected to 'midpoint - 1'

    # If the loop completes without finding the target, return None
    return None

def verify(index):
    """
    Prints whether the target was found and its index.

    Args:
    index: The index where the target was found, or None if not found.
    """
    # Check if index is not None (meaning the target was found)
    if index is not None:
        print("Target found at index", index)
    else:
        # If index is None, print that the target was not found
        print("Target not found in list")
        
# Example usage of the functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Define a list of numbers
result = binary_search(numbers, 6)  # Call binary_search to find the number 6 in the list
verify(result)  # Verify and print the result of the search

result = binary_search(numbers, 10)  # Call binary_search to find the number 6 in the list
verify(result)  # Verify and print the result of the search

result = binary_search(numbers, 13)  # Call binary_search to find the number 6 in the list
verify(result)  # Verify and print the result of the search