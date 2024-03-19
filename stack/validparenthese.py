def isValid(s):
    stack = []

    pairs = {
        '(':')', 
        '{':'}', 
        '[':']'
        
        }
    
    for bracket in s:
        if bracket in pairs: #bracket is a key
            stack.append(bracket)
        elif len(stack) == 0 or bracket != pairs[stack.pop()]:
            return False
    return len(stack) == 0
            
t = "((({{]})))"
s = "["

print(isValid(t))
print(isValid(s))