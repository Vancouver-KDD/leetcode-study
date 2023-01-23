# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


class Solution:
    def isPalindrome(self, s):
        import re
        s = re.sub(r'[^0-9a-zA-Z]', '', s).lower()
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True


    def isPalindrome_compare_reverse(self, s):
        import re
        s = re.sub(r'[^0-9a-zA-Z]', '', s).lower()
        reverse_string = s[::-1]
        return reverse_string == s