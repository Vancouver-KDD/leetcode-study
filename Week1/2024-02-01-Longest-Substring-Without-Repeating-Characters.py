class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        using sliding window technique
        using set instead of list
            time complexity for searching in a set is O(1)
            on the other hand, time complexity of searching in a list is O(n)
        """
        res = 0
        left = 0
        current = set()
        for right in range(len(s)):
            while s[right] in current:
                current.remove(s[left])
                left += 1
            current.add(s[right])
            res = max(res, right - left + 1)
           
        return res