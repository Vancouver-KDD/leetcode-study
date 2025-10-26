class Solution(object):
    def characterReplacement(self, s, k):
        from collections import Counter

        left = right = 0
        max_length = 0
        while right < len(s):
            for i in range(left, len(s)):
                while left <= right:
                    counts = Counter()
                    for char in s[i:right]:
                        counts[ord(char) - ord('A')] += 1
                    max_count = max(counts.values() or [0])

                if len(s[i:right]) - max_count <= k:
                    max_length = max(max_length, len(s[i:right]))
                right += 1
            left += 1

        return max_length
