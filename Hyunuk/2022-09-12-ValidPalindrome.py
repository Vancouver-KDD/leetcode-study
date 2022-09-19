class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if l >= r:
                break
            if s[l].lower() != s[r].lower():
                return False
            r -= 1
            l += 1
        return True
