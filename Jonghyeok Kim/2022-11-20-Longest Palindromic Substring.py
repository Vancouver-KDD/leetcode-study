class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        res, max_len = s[0], 1
        for i in range(1, len(s)):
            left, right = i-1, i
            while left > -1 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    res = s[left:right+1]
                    max_len = right - left + 1
                left -= 1
                right += 1

        if len(s) == 2:
            return res
        
        for i in range(1, len(s)-1):
            left, right = i-1, i+1
            while left > -1 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    res = s[left:right+1]
                    max_len = right - left + 1
                left -= 1
                right += 1
        return res