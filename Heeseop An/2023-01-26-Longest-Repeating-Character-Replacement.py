class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {} #frequency of each char
        result = 0
        l = 0 #left pointer

        for r in range(len(s)): #right pointer performing window slide
            charCount[s[r]] = 1 + charCount.get(s[r], 0) #increment char frequency and avoid default value error
            if (r - l + 1) - max(charCount.values()) > k:
                charCount[s[l]] -= 1
                l += 1
            result = max(result, (r - l + 1))

        return result