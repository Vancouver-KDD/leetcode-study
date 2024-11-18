class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        c = 0
        l = 0

        for r in range(len(s)):
            d[s[r]] = 1 + d.get(s[r], 0)

            if (r - l + 1) - max(d.values()) > k:
                d[s[l]] -= 1
                l += 1

            c = max(r - l + 1, c)

        return c


solution = Solution()
result = solution.characterReplacement("AABABBA", 1)
print(result)
