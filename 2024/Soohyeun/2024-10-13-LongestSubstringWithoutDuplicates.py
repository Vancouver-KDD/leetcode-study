class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        seen = set()
        max_len = 0
        left = 0

        for right, letter in enumerate(s):
            if letter in seen:
                while left < right:
                    left_letter = s[left]
                    seen.remove(left_letter)
                    left += 1
                    if left_letter == letter:
                        break
            seen.add(letter)

            max_len = max(max_len, right - left + 1)

        return max_len
