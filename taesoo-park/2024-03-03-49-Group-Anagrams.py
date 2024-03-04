class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        if len(s) != len(t):
            return False
        else:
            return s_sorted == t_sorted