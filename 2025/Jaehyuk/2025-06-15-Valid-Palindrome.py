class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        return s[::-1] == s
    

    #or

    def isPalindrome1(self, s:str) -> bool:
        s = "".join(char for char in s if char.lower().isalnum())
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True