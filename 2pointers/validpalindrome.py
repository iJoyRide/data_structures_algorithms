def isPalindrome(s):  
    newstr = ""
    for i in s:
        if i.isalnum():
            newstr += i.lower() 

    return newstr == newstr[::-1]

s = "racecar12"
t = "racecar"
print(isPalindrome(s))
print(isPalindrome(t))
