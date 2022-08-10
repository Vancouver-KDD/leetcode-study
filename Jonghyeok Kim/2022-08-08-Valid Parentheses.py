import collections

class Solution:
    def isValid(self, s: str) -> bool:
        q = collections.deque([])
        hash_map = {")":"(", "]":"[", "}":"{"}
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                q.append(ch)
            elif not q:
                return False
            elif hash_map[ch] == q[-1]:
                q.pop()
            else:
                return False
        return True if not q  else False