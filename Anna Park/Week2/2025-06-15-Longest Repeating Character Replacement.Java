class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26  # Array to count frequency of each character (only uppercase letters)
        max_count = 0  # The count of the most frequent character in the current window
        left = 0  # Left pointer of the sliding window
        res = 0  # Result to store the maximum length found

        for right in range(len(s)):
            # Update count for the current character
            count[ord(s[right]) - ord('A')] += 1

            # Update max_count if current character's frequency is higher
            max_count = max(max_count, count[ord(s[right]) - ord('A')])

            # If the remaining characters exceed k, shrink the window from the left
            while (right - left + 1) - max_count > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1  # Move the left pointer to maintain a valid window

            # Update the result with the maximum valid window length
            res = max(res, right - left + 1)

        return res
