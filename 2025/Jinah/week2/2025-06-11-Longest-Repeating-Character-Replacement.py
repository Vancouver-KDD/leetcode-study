# sliding window algorithm

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, maxCount, maxLength = 0, 0, 0
        seen = dict()
        
        for end, c in enumerate(s):
            seen[c] = seen.get(c, 0) + 1
            maxCount = max(seen[c], maxCount)

            while (end - start + 1) - maxCount > k:
                seen[s[start]] -= 1
                start += 1

        maxLength = max(maxLength, end - start + 1)
        
        return maxLength