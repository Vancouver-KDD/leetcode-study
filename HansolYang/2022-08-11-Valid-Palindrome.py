class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_s = ""
        
        for i in range(len(s)):
            c = s[i]
            if c.isalnum():
                new_s = new_s + c.lower()
        
        for i in range(len(new_s)):
            if new_s[i] != new_s[len(new_s) - 1 - i]:
                return False
        
        return True