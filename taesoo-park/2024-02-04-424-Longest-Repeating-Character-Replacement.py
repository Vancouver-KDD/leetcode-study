class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = 0
        max_length = 0
        start = 0
        letter_count = [0] * 26
        
        for end in range(len(s)):
            letter_count[ord(s[end]) - ord('A')] += 1
            max_count = max(max_count, letter_count[ord(s[end]) - ord('A')])

            while (end - start + 1 - max_count) > k:
                letter_count[ord(s[start]) - ord('A')] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length