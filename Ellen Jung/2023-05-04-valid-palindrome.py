class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = ''.join(x for x in s if x.isalnum())

        if s == "":
            return True

        for x in range (0, len(s)):
            start = s[x]
            end = s[len(s) - (1 + x)]
            if start != end:
                return False
        return True
