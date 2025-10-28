class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        left = 0
        count_letter = defaultdict(int)
        res = 0

        for right, c in enumerate(s):
            count_letter[c] += 1
            max_len = max(max_len, count_letter[c])

            while right - left + 1 > max_len + k:
                count_letter[s[left]] -= 1
                if count_letter[s[left]] == 0:
                    del count_letter[s[left]]
                left += 1
            res = max(res, right - left + 1)

        return res
