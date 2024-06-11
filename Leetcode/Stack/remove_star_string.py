def removeStar(s):
    word = []
    
    for char in s:
        if char!= "*":
            word.append(char) 
        else:
            word.pop()
    
    return "".join(word)

#Time = O(N)
#Space = O(N)

if __name__ == "__main__":
    s = "leet**cod*e"
    print(removeStar(s))