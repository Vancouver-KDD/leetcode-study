class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        left = 0
        count_letter = defaultdict(int)
        max_count_letter = 0

        for right in range(len(s)):
            count_letter[s[right]] += 1
            max_count_letter = max(max_count_letter, count_letter[s[right]])

            is_valid = (right - left + 1 - max_count_letter <= k)
            if not is_valid:
                count_letter[s[left]] -= 1
                left += 1
            max_len = right - left + 1

        return max_len
