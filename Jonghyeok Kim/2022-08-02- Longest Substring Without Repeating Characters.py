class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_loc = {}
        start = 0
        max_len = 0
        for idx, ch in enumerate(s):
            if ch in string_loc and start <= string_loc[ch]:
                start = string_loc[ch] + 1
            else:
                max_len = max(max_len, idx - start +1)
            string_loc[ch] = idx
            
        return max_len