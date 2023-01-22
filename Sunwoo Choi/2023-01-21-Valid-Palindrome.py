import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = self.clean_str(s)
        left, right = 0, len(cleaned_str) - 1
        while left < right:
            if cleaned_str[left] != cleaned_str[right]:
                return False
            left += 1
            right -= 1
        
        return True

    def clean_str(self, s: str) -> str:
        lower = s.lower()
        res = re.sub(r"[^a-z0-9]+", '', lower)
        return res
