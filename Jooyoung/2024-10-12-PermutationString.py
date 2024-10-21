from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        s1_c = Counter(s1)
        window_c = Counter()

        for i in range(m):
            window_c[s2[i]] += 1

            if i >= n:
                if window_c[s2[i - n]] == 1:
                    del window_c[s2[i - n]]
                else:
                    window_c[s2[i - n]] -= 1

            if window_c == s1_c:
                return True

        return False


solution = Solution()
result = solution.checkInclusion("adc", "dcdab")
print(result)
