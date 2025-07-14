class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        start = 0
        maxlen = 0

        for end in range(len(s)):
            while s[end] in substring:
                substring.remove(s[start])
                start += 1

            substring.add(s[end])
            maxlen = max(maxlen, end - start + 1)

        return maxlen