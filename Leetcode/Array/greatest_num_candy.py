def can_become_max(candies, extraCandies):
    # Find the maximum number of candies in the list
    max_candy = max(candies)
    
    # Initialize an empty list to store the results
    res = []
    
    # Iterate through each candy in the list
    for candy in candies:
        # Check if adding extra candies to the current candy
        # makes it greater than or equal to the maximum candy
        if (candy + extraCandies) >= max_candy:
            res.append(True)  # If yes, append True to the result list
        else:
            res.append(False)  # If no, append False to the result list
    
    # Return the list of results
    return res

#Time: O(N)
#Space: O(N)

if __name__ == "__main__":
    candies = [2,3,5,1,3]
    extraCandies = 3
    print(can_become_max(candies, extraCandies))