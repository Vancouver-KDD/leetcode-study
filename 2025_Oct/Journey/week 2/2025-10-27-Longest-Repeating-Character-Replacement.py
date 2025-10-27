from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # curr_dict: keeps count of each letter in the current window
        curr_dict = defaultdict(int)
        # left: start position of the window
        # max_len: longest valid window found so far
        left = max_len = 0

        # Move 'right' from start to end of the string
        for right in range(len(s)):
            # Add the current character to the count
            curr_dict[s[right]] += 1
            # length: size of the current window
            length = right - left + 1

            # If we need to change more than k letters to make all same,
            # move 'left' to shrink the window
            while max(curr_dict.values()) < length - k:
                curr_dict[s[left]] -= 1
                left += 1
                length -= 1

            # Update the longest valid window size
            max_len = max(max_len, right - left + 1)

        # Return the length of the longest substring we can make
        return max_len