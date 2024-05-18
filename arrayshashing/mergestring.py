
def mergeAltenately(word1, word2):
    
    merged = []
    
    for i, x in zip(word1, word2):
        merged.append(i + x)
    
    merged.append(word1[len(word2):])
    merged.append(word2[len(word1):])
    
    return "".join(merged)
    
    
    










print(mergeAltenately("abc" , "pqrs"))

