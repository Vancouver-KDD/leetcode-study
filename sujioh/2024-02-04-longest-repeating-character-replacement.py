class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        left = 0 
        right = 0 
        maxRepeatingChar = 0 

        for right in range(len(s)):
            charMap[s[right]] = 1 + charMap.get(s[right], 0)
            maxRepeatingChar = max(maxRepeatingChar, charMap[s[right]])

            # if operation needed is more than K, new sliding window
            if (right - left + 1) - maxRepeatingChar > k:
                charMap[s[left]] -= 1
                left += 1
        return right - left + 1