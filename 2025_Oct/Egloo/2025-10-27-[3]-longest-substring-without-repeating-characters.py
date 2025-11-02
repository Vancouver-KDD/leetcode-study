class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        for i in range(len(s)):
            dic = {}
            length = 0
            for j in range(i, len(s)):
                if s[j] in dic:
                    break
                dic[s[j]] = True
                length += 1
            if length > maxLen:
                maxLen = length
        return maxLen

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """


        dic = {}
        startIdx = 0
        curLen = 0
        maxLen = 0

        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= startIdx:
                curLen = i - dic[s[i]]
                startIdx = dic[s[i]]
                dic[s[i]] = i
            else:
                dic[s[i]] = i
                curLen += 1

            if curLen > maxLen:
                maxLen = curLen

        return maxLen


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        startIdx = -1
        curLen = 0
        maxLen = 0

        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= startIdx:
                startIdx = dic[s[i]]
            dic[s[i]] = i

            curLen = i - startIdx
            if curLen > maxLen:
                maxLen = curLen

        return maxLen