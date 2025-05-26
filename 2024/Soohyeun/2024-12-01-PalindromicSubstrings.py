class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def check_palindrome(left, right):
            nonlocal res
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1

        for i in range(len(s)):
            res += 1
            check_palindrome(i - 1, i + 1)
            check_palindrome(i, i + 1)

        return res
