class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for ch in s:
            if ch.isalpha():
                clean += ch.lower()
            elif ch.isnumeric():
                clean += ch
        left, right = 0, len(clean)-1
        while left <= right:
            if clean[left] == clean[right]:
                left += 1
                right -= 1
            else:
                return False
        return True