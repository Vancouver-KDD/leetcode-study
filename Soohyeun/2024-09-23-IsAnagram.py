from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = defaultdict(int)
        for i in range(len(s)):
            seen[s[i]] += 1
            seen[t[i]] -= 1
            if seen[s[i]] == 0:
                del seen[s[i]]
            if seen[t[i]] == 0:
                del seen[t[i]]

        return True if not seen else False
