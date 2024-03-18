def isValid(s):
    stack = []

    closeToOpen = {")" : "(" , "]" : "[" , "}" : "{" }

    for c in s:
        if c in closeToOpen:
            if stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False

s = "()[]{}"
t = "((({{]})))"

print(isValid(t))
print(isValid(s))