class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        l = 0
        freq = dict()
        maxFreq = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxFreq = max(maxFreq, freq[s[r]])
            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans