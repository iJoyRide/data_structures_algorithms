def largestAltitude(gain):
    """Method 1"""
    # Initialize 'highest' to track the highest altitude reached.
    # Start at 0 because the altitude starts at sea level.
    highest = 0

    # 'change' keeps track of the cumulative change in altitude.
    change = 0

    # Loop through each change in altitude in the 'gain' list.
    for i in range(len(gain)):
        # Update the current altitude based on the change.
        change += gain[i]

        # Check if the current altitude is the highest we've seen so far.
        if change > highest:
            highest = change

    # Return the highest altitude reached during the journey.
    return highest


# Time = O(N)
# Space = O(N)

if __name__ == "__main__":
    gain = [-5, 1, 5, 0, -7]
    print(largestAltitude(gain))
