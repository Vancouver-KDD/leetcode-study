class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in bracketMap:
                if stack and stack[-1] == bracketMap[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        if stack:
            return False
        else:
            return True
