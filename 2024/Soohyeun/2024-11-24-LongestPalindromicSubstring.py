class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Go through each alphabets from the very first alphabet
        # Assume it is middle of palindrom, and this will be expanded until left/right alphabets are not same
        # check if this palindrom is longest one or not

        longest_substring = ""
        longest_len = 0
        for i in range(len(s)):
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if longest_len < r - l - 1:
                longest_len = r - l - 1
                longest_substring = s[l + 1:r]

            l = i - 1
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if longest_len < r - l - 1:
                longest_len = r - l - 1
                longest_substring = s[l + 1:r]

        return longest_substring