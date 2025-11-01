def characterReplacement(self, s: str, k: int) -> int:
    left = 0
    right = 0
    currChar = [0] * 26
    currMax = 0
    longest = 0

    while right < len(s):
        index = ord(s[right]) - ord('A')
        currChar[index] += 1
        currMax = max(currMax, currChar[index])

        while right - left + 1 - currMax > k:
            currChar[ord(s[left]) - ord('A')] -= 1
            left += 1
        
        longest = max(longest, right - left + 1)
        right += 1
        
    return longest