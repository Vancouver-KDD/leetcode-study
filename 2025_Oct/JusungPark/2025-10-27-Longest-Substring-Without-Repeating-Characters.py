def lengthOfLongestSubstring(self, s: str) -> int:
    left = 0
    right = 0
    longest = 0

    currChar = set()
    while left < len(s):
        while right < len(s) and s[right] not in currChar:
            currChar.add(s[right])
            right += 1
        longest = max(longest, right - left)
        currChar.remove(s[left])
        left += 1
    
    return longest