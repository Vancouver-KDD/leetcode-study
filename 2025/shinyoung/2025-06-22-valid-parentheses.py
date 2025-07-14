def isValid(s):
    stack = []
    parent = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    # s: ]
    for c in s:
        if c == ')' or c == ']' or c == '}':
            if len(stack) > 0:
                if parent[stack.pop()] != c:
                    return False
            else:
                return False
        else:
            stack.append(c)
    return True if len(stack) == 0 else False


print(isValid("()[]{}"))
print(isValid("([])"))
print(isValid("["))
print(isValid("]"))
