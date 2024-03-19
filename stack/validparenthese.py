def isValid(s):
    stack = []

    pairs = {"(": ")", "{": "}", "[": "]"}

    for bracket in s:
        if bracket in pairs:  # bracket is a key
            stack.append(bracket) #if bracket exist, it will append to stack
        elif len(stack) == 0 or bracket != pairs[stack.pop()]: #pop the latest string from stack and check its element
            return False
    return len(stack) == 0


t = "({]})"
s = "["

print(isValid(t))
print(isValid(s))
