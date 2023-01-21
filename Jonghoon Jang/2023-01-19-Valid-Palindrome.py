"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    # Two Pointer
    # Time complexity: O(N): traverse each char at most once
    # Space complexity: O(1): no extra space needed
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:  # until the pointers meet in the middle
            if not s[l].isalnum():  # ignore non-alphanumeric char
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False
            else: # traverse inwards
                l += 1
                r -= 1
        return True

    # Two Pointer
    # Time complexity: O(N): traverse each char linearly
    # Space complexity: O(N): extra space to store filtered string
    def isPalindromeReverse(self, s: str) -> bool:
        filtered_s = [char.lower() for char in s if char.isalnum()]
        return filtered_s == filtered_s[::-1]


def main():
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindromeReverse("A man, a plan, a canal: Panama"))

    print(s.isPalindrome("race a car"))
    print(s.isPalindromeReverse("race a car"))

    print(s.isPalindrome(" "))
    print(s.isPalindromeReverse(" "))



if __name__ == "__main__":
    main()
