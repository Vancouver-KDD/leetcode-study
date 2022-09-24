class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_valid():
            for i in chars:
                if freq[i] > 0:
                    return False
            return True
            
        if not t or not s or len(t) > len(s):
            return ""
        ret = ""
        l, r = 0, 0
        freq = collections.Counter(t)
        chars = set(t)
        while r < len(s):
            freq[s[r]] -= 1
            while l <= r and is_valid():
                if not ret:
                    ret = s[l:r+1]
                else:
                    ret = min(ret, s[l:r+1], key=len)
                freq[s[l]] += 1
                l += 1
            r += 1
        return ret
