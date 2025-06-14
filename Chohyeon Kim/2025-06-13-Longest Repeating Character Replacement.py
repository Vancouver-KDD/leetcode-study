class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        frequency_count = {}
        max_longest = 0

        l = 0

        # A B A B
        # l
        #       r
        # 1 2
        # 1 2

        for r in range(len(s)):

            if s[r] not in frequency_count:
                frequency_count[s[r]] = 1
            else:
                frequency_count[s[r]] += 1

            if r - l + 1 - max(frequency_count.values()) > k:
                frequency_count[s[l]] -= 1
                l += 1

            max_longest = max(max_longest, r - l + 1)

        print(frequency_count)

        return max_longest
