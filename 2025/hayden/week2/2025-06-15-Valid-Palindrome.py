class Solution:
    def isPalindrome(self, s: str) -> bool:

        #filtering everything first. No puncuations. Only numbers and letters.
        filtered = ''.join(c.lower() for c in s if c.isalnum())

        reverse = filtered[::-1]

        if reverse == filtered:
            return True
        return False
        