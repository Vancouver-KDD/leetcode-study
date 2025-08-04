class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        save = set()
        max_len = 0
        left = 0
        for i in range(len(s)):
            while s[i] in save :
                save.remove(s[left])
                left += 1
            save.add(s[i])
            max_len = max(max_len, i - left + 1)
            print(save, max_len)
        return max_len
