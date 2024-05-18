def linear_search(list, target):
    """
    Performs a linear search for the target in the list.

    Args:
    list: The list in which to search for the target.
    target: The target value to search for.

    Returns:
    int: The index of the target if found, else None.
    """
    # Iterate over each index from 0 to the length of the list - 1
    for i in range(0, len(list)):
        # Check if the element at the current index is equal to the target
        if list[i] == target:
            # If found, return the index
            return i
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
result = linear_search(numbers, 6)  # Call linear_search to find the number 6 in the list
verify(result)  # Verify and print the result of the search

result = linear_search(numbers, 10)  # Call linear_search to find the number 6 in the list
verify(result)  # Verify and print the result of the search

result = linear_search(numbers, 13)  # Call linear_search to find the number 6 in the list
verify(result)  # Verify and print the result of the search

# Output
# Target found at index 5
# Target found at index 9
# Target not found in list