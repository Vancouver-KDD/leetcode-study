class Solution:
    def countSubstrings(self, s: str) -> int:
        def findPalindrom(left, right):
            num = 0
            while left >= 0 and right < len(s) and s[left] == s [right]:
                num += 1
                left -= 1
                right += 1
            return num

        num_substrings = 0
        for i, char in enumerate(s):
            odd = findPalindrom(i-1, i+1)
            even = findPalindrom(i, i+1)
            num_substrings += (odd + even + 1)

        return num_substrings
    