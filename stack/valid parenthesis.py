def isValid( s):
    stack = []
    closeOpen = {"}": "{", ")": "(", "]": "["}

    for c in s:
        if c in closeOpen:
            if stack and stack[-1] == closeOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False


s= "[]"
print(isValid(s))