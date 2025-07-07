class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Declare variables to store character counts, maximum length of substring, and sliding window indices
        char_count = {s[0] : 1}
        max_length = 0
        left, right = 0, 1
        # Iterate process of incrementing window indices while upperbound is less than the length of string
        while right < len(s):
            # Calculate the max frequency of characters
            most_frequent = max(char_count.values())
            # Check if k is bigger than the number of characters other than the most frequent
            if right - left - most_frequent <= k:
                # Update max length
                max_length = max(max_length, right - left)
                # Increment upperbound and increment the character count
                right += 1
                char_count[s[right - 1]] = char_count.get(s[right - 1], 0) + 1
            else:
                # Decrement lowerbound character count and index
                char_count[s[left]] -= 1
                left += 1
        # One additional calculation outside loop
        most_frequent = max(char_count.values())
        if right - left - most_frequent <= k:
            max_length = max(max_length, right - left)
        # Return max length of substring
        return max_length
