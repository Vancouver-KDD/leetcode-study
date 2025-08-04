class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        stack = []
        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif not stack or pairs[char] != stack.pop():
                return False
        return False if stack else True