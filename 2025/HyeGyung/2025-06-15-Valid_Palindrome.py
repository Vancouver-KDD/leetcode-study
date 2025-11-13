class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean_s = "".join((char for char in s if char.isalnum()))
        print(clean_s)
        clean_s = clean_s.lower()
        reverse = clean_s[::-1]
        isPalindrome = True if (clean_s == reverse) else False
        return isPalindrome
