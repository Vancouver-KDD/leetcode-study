def longestSub(self, s, k):
    count = {}
    res = 0

    l = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        windowSize = r - 1 + 1
        while windowSize - max(count.values()) > k:
            count[s[r]] -= 1
            l += 1

        res = max(res, windowSize)

    return res
