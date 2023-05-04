class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) < 1 or len(t) > 5 * 10 ** 4:
            raise ValueError

        for x in s:
            if x in t:
                t.replace(x, '')
            else:
                return False
        return True
