class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n_s = sorted(s)
        n_t = sorted(t)
        if len(n_s) != len(n_t):
            return False
        if n_s == n_t:
            return True
            