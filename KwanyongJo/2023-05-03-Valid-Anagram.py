# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic1 = {}
        dic2 = {}

        for i in range(len(s)):
            if s[i] in dic1:
                dic1[s[i]] += 1
            else:
                dic1[s[i]] = 1
        for i in range(len(t)):
            if t[i] in dic2:
                dic2[t[i]] += 1
            else:
                dic2[t[i]] = 1

        if dic1 == dic2 :
            return True
        else:
            return False


# if __name__ == '__main__':
#     s = Solution()
#
#     print(s.isAnagram('aacc', 'ccac'))

