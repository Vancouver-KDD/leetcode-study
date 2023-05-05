# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Constraints:
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # To solve the problem we can use 2 pointers
        # Start one pointer at the beginning of the string, and the other at the end
        # If the character at the current index is not an alphabet or number character, move the pointer either to the right or to the left
        # Else, compare the two characters to see if it is the same or not
        # Note: even though s consists only of printable ASCII characters, it does not include punctuations, also characters are not case sensitive

        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True
