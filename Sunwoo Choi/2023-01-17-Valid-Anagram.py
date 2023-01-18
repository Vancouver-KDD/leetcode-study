class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_chars = {}
        for c in s:
            s_chars[c] = 1 + s_chars[c] if c in s_chars else 1

        for c in t:
            if c not in s_chars:
                return False
            else:
                s_chars[c] -= 1
                if s_chars[c] == 0:
                    del s_chars[c]
        
        return not s_chars
