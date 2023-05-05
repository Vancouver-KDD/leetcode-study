# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters,
# it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Uppercase -> Lowercase

        lowerStr = s.lower()

        #using isalpha() and isnumeric() to leave the only alphabets and numbers
        newStr = list([val for val in lowerStr
                       if val.isalpha() or val.isnumeric()])

        result = "".join(newStr)

        if len(result) == 0 or len(result) == 1:
            return True

        #abcde  abba
        length_result = len(result)
        for i in range(len(result)):
            if length_result - i >= 0:
                if result[i] != result[len(result)-1-i]:
                    return False
        return True


