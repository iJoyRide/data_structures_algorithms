def guess(num):
    """
    Function to compare the guessed number with the target number.

    Args:
    - num: The number guessed by the algorithm.

    Returns:
    - -1 if the guessed number is higher than the target.
    - 1 if the guessed number is lower than the target.
    - 0 if the guessed number is equal to the target.
    """
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


def guessNumber(n):
    """
    Binary search algorithm to guess the target number within a given range.

    Args:
    - n: The upper limit of the range to search within.

    Returns:
    - The target number if found within the range.
    """
    x = guess(n)

    if x == 0:
        return n

    low = 0
    high = n

    while low <= high:
        # Calculate the middle of the current search range
        middle = ((high - low) // 2) + low

        # Check the guessed number against the target number
        match = guess(middle)

        if match == 0:
            # If the guessed number is equal to the target, return it
            return middle

        elif match == -1:
            # If the guessed number is higher than the target, adjust the high end of the search range
            high = middle - 1

        else:
            # If the guessed number is lower than the target, adjust the low end of the search range
            low = middle + 1
            
#Time: O(log n)
#Space: O(1)

if __name__ == "__main__":

    pick = 4

    pick_num_1_to_n = 50

    print(guessNumber(pick_num_1_to_n))
