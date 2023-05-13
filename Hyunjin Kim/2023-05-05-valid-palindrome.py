class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(i for i in s if i.isalnum()).lower()

        return s == s[::-1]
