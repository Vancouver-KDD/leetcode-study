class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26  
        max_count = 0  # 현재 윈도우 내에서 가장 많이 등장한 문자 수
        left = 0
        res = 0

        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1
            max_count = max(max_count, count[ord(s[right]) - ord('A')])

            while (right - left + 1) - max_count > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res