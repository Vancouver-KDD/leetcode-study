class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_p = ['{', '(', '[']
        close_p = ['}', ')', ']']
        for ch in s:
            if ch in open_p:
                stack.append(ch)
            elif ch in close_p:
                i = close_p.index(ch)
                if len(stack) == 0:
                    return False
                if stack.pop() != open_p[i]:
                    return False
        if len(stack) != 0:
            return False
        return True