def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:  # If the character is a closing bracket
            top_element = stack.pop() if stack else '#'  # Pop the top element from the stack if available, otherwise use '#'
            if mapping[char] != top_element:
                return False
        else:  # If the character is an opening bracket
            stack.append(char)

    return not stack  # If the stack is empty, all open brackets have their corresponding closed brackets
