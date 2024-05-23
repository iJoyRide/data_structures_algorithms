def maxVowels(s, k):
    """Method 1"""

    # Initialise vowels
    vowels = ["a", "e", "i", "o", "u"]
    count_vows = 0
    max_vows = 0
    left = 0

    for right in range(len(s)):

        # If right of window in vowels, increase count of vowels by 1
        if s[right] in vowels:
            count_vows += 1
        
        # Size of window
        vows = right - left + 1
        
        # If size of window > k, enter loop
        if vows > k:
            if s[left] in vowels:
                count_vows -= 1

            left += 1

        # Take the max size of window or count of vowels
        max_vows = max(max_vows, count_vows)

    return max_vows

#Time = O(N)
#Space = O(1)

def maxVowels2(s, k):
    """Method 2"""
    
    vowels = set("aeiou")  # Using set for faster lookup
    count_vows = 0
    max_vows = 0
    left = 0

    for right in range(len(s)):
        if s[right] in vowels:
            count_vows += 1

        if right - left + 1 > k:
            if s[left] in vowels:
                count_vows -= 1
            left += 1

        max_vows = max(max_vows, count_vows)

    return max_vows


if __name__ == "__main__":

    s = "abciiidef"
    k = 3
    print(maxVowels(s, k))
    
    s2 = "aeiou"
    k2 = 3
    print(maxVowels2(s2, k2))

#Time = O(N)
#Space = O(1)