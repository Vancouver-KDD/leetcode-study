class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)