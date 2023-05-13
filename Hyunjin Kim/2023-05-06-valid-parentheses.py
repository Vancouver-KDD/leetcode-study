def isValid(self, s):
    pair = {")": "(", "]": "[", "}": "{"}
    stack = []
    for i in s:
        if i in pair:
            if stack:
                # if something in stack, pop it to compare
                last_element = stack.pop()
            else:
                # for handling the cases where the stack is empty
                last_element = '#'
            if pair[i] != last_element:
                return False
        else:
            stack.append(i)
    return len(stack) == 0
