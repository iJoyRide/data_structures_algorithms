def reverseWords(s):
    """Method 1: My method"""

    # Initialise the list
    reverseword = []

    # Split the string into a list, already removes the empty space
    word = s.split()

    # Find the size of the list: 4
    array_size = len(word)

    # Iterate through the list
    for i in range(array_size):

        # Append last element
        reverseword.append(word[array_size - i - 1])

    # Return the entire string with space
    return " ".join(reverseword)

    #Time: O(N)
    #Space: O(N)

def shortReverseWords(s):
    """Mehtod 2"""
   
    # Split the string into a list, already removes the empty space
    s = s.split()
    
    # Reverse the list using slicing
    # Start from the end and go all the way to the beginning
    s = s[::-1]
    
    # Return the entire string with space
    return " ".join(s)

    #Time: O(N)
    #Space: O(N)

if __name__ == "__main__":

    print(reverseWords("the    sky is    blue"))
    print(shortReverseWords("nice    can of    coke"))
