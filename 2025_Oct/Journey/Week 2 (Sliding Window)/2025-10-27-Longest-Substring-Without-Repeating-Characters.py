class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left: start of the window
        # max_len: the longest length found so far
        # chr_set: stores the characters in the current window
        left = max_len = 0
        chr_set = set()

        # Move 'right' from the start to the end of the string
        for right in range(len(s)):
            # If the character already exists in the set,
            # remove characters from the left side until it's gone
            while s[right] in chr_set:
                chr_set.remove(s[left])
                left += 1

            # Add the current character to the set
            chr_set.add(s[right])

            # Update the longest length if needed
            max_len = max(max_len, right - left + 1)

        # Return the longest substring length with no repeat characters
        return max_len