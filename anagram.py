s = "anagram"
t = "nagaram"

if len(s) != len(t):
    print(False)
elif sorted(s) == sorted(t):
    print(True)
    
    