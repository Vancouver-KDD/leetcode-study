class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        hashMap = {")":"(", "}":"{", "]":"["}
        stack = []
        for c in s:
            if c not in hashMap:
                stack.append(c)
                continue
            if not stack or stack.pop() != hashMap[c]:
                return False
        return not stack