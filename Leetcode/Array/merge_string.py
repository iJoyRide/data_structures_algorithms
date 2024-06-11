def mergeAlternately(word1, word2):
    """Method 1"""

    # Initialise empty string
    merged = []

    # Calculates the min length between the two words, which is 3
    min_len = min(len(word1), len(word2))

    # Iterates "i" over the range of min_len
    for i in range(min_len):

        # Append the ith character of word1 and word2, ['ap', 'bq', 'cr']
        merged.append(word1[i] + word2[i])

    # Append the remaining the character to the end of the list, ['12345']
    merged.extend(word1[min_len:])
    merged.extend(word2[min_len:])

    # ['ap', 'bq', 'cr', '12345']

    # Joins all the elements of the "merged" list into a
    # single string with empty string, ['adbecf12345']
    return "".join(merged)

    # Time: 0(N)
    # Space: 0(N)


if __name__ == "__main__":
    print(mergeAlternately("abc", "def12345"))

