def isPalindrome(s):  
    newstr = ""
    for i in s:
        if i.isalnum():
            newstr += i.lower() 

    return newstr == newstr[::-1]

s = "race car12"
t = "racec ar"
print(isPalindrome(s))
print(isPalindrome(t))
