class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        s_chars = list(s)
        counts = [0] * 26
        max_length = 0
        unique_chars, k_or_more_chars = 0, 0

        for unique_count in range(1, 27):
            counts = [0] * 26
            left, right = 0, 0
            unique_chars, k_or_more_chars = 0, 0

            while right < len(s):
                if unique_chars <= unique_count:
                    char_idx = ord(s_chars[right]) - ord('a')
                    counts[char_idx] += 1

                    if counts[char_idx] == 1:
                        unique_chars += 1
                    if counts[char_idx] == k:
                        k_or_more_chars += 1

                    right += 1
                else:
                    char_idx = ord(s_chars[left]) - ord('a')

                    if counts[char_idx] == k:
                        k_or_more_chars -= 1
                    counts[char_idx] -= 1

                    if counts[char_idx] == 0:
                        unique_chars -= 1

                    left += 1

                if unique_chars == unique_count and k_or_more_chars == unique_count:
                    max_length = max(max_length, right - left)

        return max_length
