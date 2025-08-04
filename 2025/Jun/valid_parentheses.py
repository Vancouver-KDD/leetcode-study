class Solution:
    def isValid(self, s: str) -> bool:
        map = {'(' : ')', "{" : "}", "[" : "]"}
        stack = []
        for char in s:
            if char in map:
                stack.append(char)
            else:
                if not stack:
                    return False
                openP = stack.pop()
                if map[openP] is not char:
                    return False

        return len(stack) is 0