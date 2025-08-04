# Time: 7 ms (81.52%), Space: 18.1 MB (69.4%)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1

        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1

            if s[start].lower() != s[end].lower():
                return False
            
            start += 1
            end -= 1

        return True